"""Portable regression tests for the repository checker; no model or network calls."""
import importlib.util
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_package.py"
spec = importlib.util.spec_from_file_location("check_package", SCRIPT)
checker = importlib.util.module_from_spec(spec)
spec.loader.exec_module(checker)


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        for name in ("component-doc-writer", "component-doc-visuals", "component-doc-assembler"):
            self.write(f"{name}/SKILL.md", f"---\nname: {name}\ndescription: Test fixture.\n---\n")
        self.write("LICENSE", "MIT License\nCopyright (c) 2026 Test Author\n")
        self.write("shared/example.json", "{}")
        self.write("assets/preview.svg", '<svg xmlns="http://www.w3.org/2000/svg"/>')
        self.write("README.md", "[Example](shared/example.json)\n")

    def write(self, relative, content):
        path = self.root / relative
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content, encoding="utf-8")
        return path

    def errors(self, terms=()):
        return checker.check(self.root, list(terms), release=True)

    def assert_rejected(self, message, terms=()):
        self.assertTrue(any(message in error for error in self.errors(terms)), self.errors(terms))

    def test_clean_package(self):
        self.assertEqual([], self.errors())

    def test_invalid_json(self):
        self.write("shared/example.json", "{broken")
        self.assert_rejected("Invalid JSON")

    def test_invalid_svg(self):
        self.write("assets/preview.svg", "<svg>")
        self.assert_rejected("Invalid SVG")

    def test_missing_link(self):
        self.write("README.md", "[Missing](missing.md)")
        self.assert_rejected("Broken or escaping link")

    def test_link_outside_package(self):
        self.write("README.md", "[Outside](../outside.md)")
        self.assert_rejected("Broken or escaping link")

    def test_private_term_is_case_insensitive(self):
        self.write("fixture.md", "PrIvAtE-FiXtUrE")
        self.assert_rejected("Forbidden term", ["private-fixture"])

    def test_missing_license(self):
        (self.root / "LICENSE").unlink()
        self.assert_rejected("Release requires LICENSE")

    def test_missing_skill(self):
        (self.root / "component-doc-writer/SKILL.md").unlink()
        self.assert_rejected("Expected exactly three")

    def test_mismatched_skill_name(self):
        self.write("component-doc-writer/SKILL.md", "---\nname: other-name\ndescription: Test.\n---\n")
        self.assert_rejected("Skill name differs from folder")

    def test_file_symlink_requires_review(self):
        (self.root / "linked.md").symlink_to("README.md")
        self.assert_rejected("Symlink requires manual review")

    def test_directory_symlink_requires_review(self):
        (self.root / "linked-assets").symlink_to("assets", target_is_directory=True)
        self.assert_rejected("Symlink requires manual review")

    def test_git_and_python_cache_are_not_package_assets(self):
        for relative in (".git/index", "scripts/__pycache__/checker.pyc"):
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(b"\xff\xfe\x00")
        self.assertEqual([], self.errors())

    def test_binary_package_asset_is_still_flagged(self):
        path = self.root / "assets" / "opaque.bin"
        path.write_bytes(b"\xff\xfe\x00")
        self.assert_rejected("Binary or unreadable file")


if __name__ == "__main__":
    unittest.main()
