#!/usr/bin/env python3
"""Map source property keys and check exact identifiers in Markdown drafts."""
import argparse
import json
import re
from pathlib import Path

SUFFIX = re.compile(r"#[0-9]+:[0-9]+$")
CODE = re.compile(r"(?<!`)`([^`\n]+)`(?!`)")

def public_name(raw):
    return SUFFIX.sub("", raw)

def read_spec(path):
    spec = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(spec, dict) or set(spec) - {"properties", "exact", "literals"}:
        raise ValueError("Expected an object containing properties, exact, and/or literals.")
    for role in ("properties", "exact", "literals"):
        values = spec.setdefault(role, [])
        if not isinstance(values, list) or any(not isinstance(x, str) or not x for x in values):
            raise ValueError(f"{role} must be a list of nonempty strings.")
    for raw in spec["properties"]:
        if not public_name(raw):
            raise ValueError("Property key has no public name: " + raw)
    return spec

def mapping(spec):
    return [{"raw": raw, "public": public_name(raw)} for raw in spec["properties"]]

def check(spec, text):
    codes = set(CODE.findall(text))
    errors = []
    for row in mapping(spec):
        if row["public"] not in codes:
            errors.append("Missing exact public property in a code span: " + row["public"])
        if row["raw"] != row["public"] and row["raw"] in text and row["raw"] not in spec["literals"]:
            errors.append("Raw API property key leaked into publication: " + row["raw"])
    for value in spec["exact"]:
        if value not in codes:
            errors.append("Missing exact identifier/configuration in a code span: " + value)
    for value in spec["literals"]:
        if value not in text:
            errors.append("Missing or changed literal content: " + value)
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path)
    parser.add_argument("drafts", type=Path, nargs="*")
    parser.add_argument("--map-only", action="store_true")
    args = parser.parse_args()
    try:
        spec = read_spec(args.spec)
        if args.map_only:
            if args.drafts:
                parser.error("--map-only does not accept draft files")
            print(json.dumps(mapping(spec), ensure_ascii=False, indent=2))
            return 0
        if not args.drafts:
            parser.error("Provide drafts to check, or use --map-only")
        results = []
        for draft in args.drafts:
            results.append({"file": str(draft), "errors": check(spec, draft.read_text(encoding="utf-8"))})
        print(json.dumps(results, ensure_ascii=False, indent=2))
        return int(any(item["errors"] for item in results))
    except (OSError, ValueError) as exc:
        print(str(exc))
        return 2

if __name__ == "__main__":
    raise SystemExit(main())
