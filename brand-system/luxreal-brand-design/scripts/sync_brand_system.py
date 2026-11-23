#!/usr/bin/env python3
"""Regenerate Skill references from the adjacent LuxReal brand source."""
import argparse
import hashlib
import json
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / "LuxReal_Brand_System.md"


def dump(value):
    return json.dumps(value, ensure_ascii=False, indent=2) + "\n"


def build():
    source_bytes = SOURCE.read_bytes()
    source = source_bytes.decode("utf-8")
    meta = re.search(r"版本.*?v([\d.]+)\s*·\s*(\d{4}-\d{2}-\d{2})", source)
    if not meta:
        raise ValueError("Missing source version/date")
    version, date = meta.groups()
    headings = list(re.finditer(r"^## (\d+)\..*$", source, re.M))
    sections = {
        int(m.group(1)): source[m.start():headings[i+1].start() if i+1 < len(headings) else len(source)].strip()
        for i, m in enumerate(headings)
    }
    output = {}
    groups = {
        "brand-rules.md": ("LuxReal 品牌规则与栏目约束", [1, 2, 3, 4, 5, 6, 8, 10]),
        "design-workflow.md": ("LuxReal 视觉理念、版式与执行流程", [7, 9, 11, 16]),
        "acceptance.md": ("LuxReal 输出验收", [15]),
    }
    for name, (title, ids) in groups.items():
        toc = "\n".join("- " + sections[i].splitlines()[0][3:] for i in ids)
        intro = (
            f"# {title}\n\n来源：LuxReal_Brand_System.md v{version}，{date}；由 scripts/sync_brand_system.py 按原文分节同步。\n\n"
            "按原文保留章节号。跨节查阅：第 1–6、8、10 节见 brand-rules.md；第 7、9、11、16 节见 design-workflow.md；"
            "第 12–14 节分别见 design-tokens.json、logo-manifest.json、template-slots.json；第 15 节见 acceptance.md。"
            "资源是否随包可用以 resource-status.json 和实际文件为准，不能由源文档历史缺项推断。\n\n"
            f"## 内容索引\n\n{toc}\n\n"
        )
        output[ROOT / "references" / name] = intro + "\n\n".join(sections[i] for i in ids) + "\n"

    def block(section):
        return json.loads(re.search(r"```json\n(.*?)\n```", sections[section], re.S).group(1))

    inventory = json.loads((ROOT / "references/resource-status.json").read_text())
    inventory.update(brandSourceVersion=version, brandSourceDate=date,
                     brandSourceSha256=hashlib.sha256(source_bytes).hexdigest())
    # Record actual files; retain license text and never infer usage approval.
    families = []
    for folder in sorted((ROOT / "assets/fonts").glob("HarmonyOS_Sans_*")):
        files = [{"path": str(p.relative_to(ROOT)), "sha256": hashlib.sha256(p.read_bytes()).hexdigest()}
                 for p in sorted(folder.glob("*.ttf"))]
        if not files:
            continue
        license_path = folder / "LICENSE.txt"
        families.append({"family": folder.name.replace("_", " "), "files": files,
                         "licensePath": str(license_path.relative_to(ROOT)) if license_path.is_file() else None,
                         "licenseSha256": hashlib.sha256(license_path.read_bytes()).hexdigest() if license_path.is_file() else None})
    inventory["fonts"] = {"family": "HarmonyOS Sans SC", "availability": "provided" if families else "not_provided",
                          "licenseStatus": "provided" if families and all(f["licensePath"] for f in families) else "not_provided",
                          "families": families, "usageRightsRequireVerification": True,
                          "note": "SC is the simplified-Chinese body default; TC supports traditional Chinese. Creative headlines may use other available fonts or lettering assets. License presence is not blanket usage approval."}

    tokens = block(12)
    tokens["assets"].update(fontAvailability=inventory["fonts"]["availability"],
                             fontLicenseStatus=inventory["fonts"]["licenseStatus"],
                             resourceStatusPath="references/resource-status.json")
    manifest = block(13)
    manifest["sourceRootRelativeToProject"] = manifest["rootRelativeToProject"]
    manifest["rootRelativeToProject"] = "."
    manifest["rootRelativeToSkill"] = "."
    for entry in manifest["entries"]:
        entry["sourcePath"] = entry["path"]
        entry["path"] = "assets/logos/" + Path(entry["path"]).name
    manifest["note"] = "Paths resolve from the skill root. Original PNG bytes are unchanged. Only entries with defaultAllowed=true are defaults. Verify backgrounds and clear space."
    for name, data in [("design-tokens.json", tokens), ("logo-manifest.json", manifest),
                       ("template-slots.json", block(14)), ("resource-status.json", inventory)]:
        output[ROOT / "references" / name] = dump(data)
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report stale generated references without changing files")
    args = parser.parse_args()
    stale = []
    for path, content in build().items():
        if not path.exists() or path.read_text() != content:
            stale.append(path.name)
            if not args.check:
                path.write_text(content)
    if args.check and stale:
        raise SystemExit("Stale references: " + ", ".join(stale))
    print("PASS: references match the brand source." if args.check else "Updated: " + ", ".join(stale))


if __name__ == "__main__":
    main()
