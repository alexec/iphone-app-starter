#!/usr/bin/env python3
"""Fills this template's placeholders with sample values, as Agents' make_app_repository
fills them with the person's, so the template's CI checks what a new app gets. It fails if a
placeholder is left. Run it from the repository's root: python3 .github/template/fill.py"""
import pathlib
import re
import sys

SAMPLE = {
    "APP_NAME": "Tide Log",
    "BUNDLE_ID": "com.example.tidelog",
    "SERVICE": "tidelog",
    "GCP_PROJECT": "tidelog-1234",
    "GCP_REGION": "us-central1",
    "GITHUB_REPO": "someone/tidelog",
}
PLACEHOLDER = re.compile(rb"__([A-Z][A-Z0-9_]*)__")

root = pathlib.Path(".")
ignored = [".starterignore"] + [
    line.strip().strip("/")
    for line in (root / ".starterignore").read_text().splitlines()
    if line.strip() and not line.startswith("#")
]


def skip(rel: str) -> bool:
    return rel.startswith(".git/") or any(rel == i or rel.startswith(i + "/") for i in ignored)


left = 0
for path in sorted(p for p in root.rglob("*") if p.is_file()):
    rel = path.as_posix()
    if skip(rel):
        continue
    data = path.read_bytes()
    if b"\0" in data:  # an image is not filled
        continue
    for m in PLACEHOLDER.finditer(data):
        if m.group(1).decode() not in SAMPLE:
            print(f"::error file={rel}::{m.group(0).decode()} has no sample value")
            left = 1
    path.write_bytes(PLACEHOLDER.sub(lambda m: SAMPLE.get(m.group(1).decode(), m.group(0).decode()).encode(), data))
sys.exit(left)
