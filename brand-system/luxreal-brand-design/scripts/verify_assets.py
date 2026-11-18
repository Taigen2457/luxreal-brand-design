#!/usr/bin/env python3
"""Verify packaged LuxReal resources without changes or third-party packages."""
import hashlib
import json
from pathlib import Path
import struct
import sys


def main():
    root = Path(__file__).resolve().parents[1]
    refs = root / "references"
    inventory = json.loads((refs / "resource-status.json").read_text())
    manifest = json.loads((refs / "logo-manifest.json").read_text())
    errors, indexed = [], {}
    for item in inventory["logos"] + [inventory["visManual"]]:
        path = root / item["path"]
        if not path.is_file():
            errors.append(f"Missing: {item['path']}")
            continue
        data = path.read_bytes()
        if hashlib.sha256(data).hexdigest() != item["sha256"]:
            errors.append(f"SHA-256 mismatch: {item['path']}")
        if path.suffix.lower() == ".png":
            if len(data) < 24 or data[:8] != b"\x89PNG\r\n\x1a\n":
                errors.append(f"Invalid PNG header: {item['path']}")
                continue
            size = struct.unpack(">II", data[16:24])
            if size != (item["pixelWidth"], item["pixelHeight"]):
                errors.append(f"Dimension mismatch: {item['path']}")
            indexed[item["path"]] = item
    for entry in manifest["entries"]:
        item = indexed.get(entry["path"])
        if item is None:
            errors.append(f"Unbundled manifest entry: {entry['id']}")
            continue
        for field in ("sha256", "pixelWidth", "pixelHeight", "defaultAllowed"):
            if entry[field] != item[field]:
                errors.append(f"Manifest/inventory mismatch: {entry['id']} {field}")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"PASS: {len(inventory['logos'])} original Logo PNGs and VIS verified.")
    print("Fonts: " + inventory["fonts"]["availability"])
    print("Not checked: layout quality, visible bounds, permissions or export readiness.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
