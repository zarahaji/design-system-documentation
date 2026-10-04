#!/usr/bin/env python3
"""Check a skill-set directory before public distribution (standard library only)."""

import argparse
import hashlib
import json
import os
import re
import sys
from pathlib import Path
from xml.etree import ElementTree


FRONTMATTER = re.compile(r"\A---\n(?P<body>.*?)\n---\n", re.DOTALL)
LOCAL_LINK = re.compile(r"\[[^]]*\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]*)?\)")
IGNORED_DIRECTORIES = {".git", "__pycache__"}


def package_files(root: Path) -> list[Path]:
    """List package files without following symlinks or inspecting Git internals."""
    files = []
    for directory, subdirs, filenames in os.walk(root, followlinks=False):
        parent = Path(directory)
        kept = []
        for name in subdirs:
            path = parent / name
            if path.is_symlink():
                files.append(path)
            elif name not in IGNORED_DIRECTORIES:
                kept.append(name)
        subdirs[:] = kept
        files.extend(parent / name for name in filenames)
    return sorted(files)


SKILL_NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def check(root: Path, forbidden: list[str], release: bool = False) -> list[str]:
    errors = []
    files = package_files(root)
    if not files:
        return ["Package contains no files"]
    reviewed = {}
    manifest = root / "assets/reviewed-images.json"
    if manifest.is_file() and not manifest.is_symlink():
        try:
            reviewed = json.loads(manifest.read_text(encoding="utf-8"))
            if not isinstance(reviewed, dict) or not all(isinstance(k, str) and isinstance(v, str) for k, v in reviewed.items()):
                errors.append("Invalid reviewed-image manifest")
                reviewed = {}
        except (ValueError, OSError):
            errors.append("Invalid reviewed-image manifest")
    for path in files:
        relative = path.relative_to(root)
        if path.is_symlink():
            errors.append(f"Symlink requires manual review: {relative}")
            continue
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError):
            # Only exact, manually inspected PNG bytes can bypass text scanning.
            try:
                data = path.read_bytes()
            except OSError:
                data = b""
            digest = reviewed.get(relative.as_posix())
            if not (relative.parts[0] == "assets" and path.suffix.lower() == ".png"
                    and data.startswith(b"\x89PNG\r\n\x1a\n")
                    and digest == hashlib.sha256(data).hexdigest()):
                errors.append(f"Binary or unreadable file requires manual review: {relative}")
            for term in forbidden:
                if term.casefold() in relative.as_posix().casefold():
                    errors.append(f"Forbidden term found in {relative}: {term}")
            continue
        for term in forbidden:
            if term.casefold() in f"{relative}\n{content}".casefold():
                errors.append(f"Forbidden term found in {relative}: {term}")
        if path.suffix == ".json":
            try:
                json.loads(content)
            except json.JSONDecodeError as exc:
                errors.append(f"Invalid JSON in {relative}: {exc}")
        if path.suffix == ".svg":
            try:
                ElementTree.fromstring(content)
            except ElementTree.ParseError as exc:
                errors.append(f"Invalid SVG in {relative}: {exc}")
        if path.suffix == ".md":
            for match in LOCAL_LINK.finditer(content):
                target = (path.parent / match.group(1)).resolve()
                if not target.is_relative_to(root.resolve()) or not target.exists():
                    errors.append(f"Broken or escaping link in {relative}: {match.group(1)}")
        if path.name == "SKILL.md":
            match = FRONTMATTER.match(content)
            if not match:
                errors.append(f"Missing YAML frontmatter: {relative}")
                continue
            fields = dict(re.findall(r"^(name|description):\s*(.+)$", match.group("body"), re.MULTILINE))
            if not SKILL_NAME.fullmatch(fields.get("name", "")):
                errors.append(f"Invalid skill name: {relative}")
            if fields.get("name") != path.parent.name:
                errors.append(f"Skill name differs from folder: {relative}")
            if not fields.get("description"):
                errors.append(f"Missing description: {relative}")
    if sum(path.name == "SKILL.md" for path in files) != 3:
        errors.append("Expected exactly three SKILL.md files")
    if release:
        license_path = root / "LICENSE"
        if not license_path.is_file() or (root / "LICENSE.template").exists():
            errors.append("Release requires LICENSE and no LICENSE.template")
        elif "[copyright holder]" in license_path.read_text(encoding="utf-8").casefold():
            errors.append("Release LICENSE still has an unfilled copyright holder")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("root", type=Path)
    parser.add_argument("--forbid", action="append", default=[], help="Case-insensitive private term to reject")
    parser.add_argument("--release", action="store_true", help="Also require a completed LICENSE")
    args = parser.parse_args()
    problems = check(args.root, args.forbid, args.release)
    for problem in problems:
        print(problem, file=sys.stderr)
    if problems:
        return 1
    print("Package structure, local links, JSON, and supplied term scan passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
