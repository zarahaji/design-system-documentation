"""Regression tests for source-key normalization and publication leakage."""
import importlib.util
import json
import tempfile
import unittest
from pathlib import Path

SCRIPT=Path(__file__).resolve().parents[1]/"component-doc-writer/scripts/check_identifiers.py"
spec=importlib.util.spec_from_file_location("identifiers",SCRIPT)
module=importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

class IdentifierChecks(unittest.TestCase):
    def test_only_terminal_numeric_suffix_is_removed(self):
        self.assertEqual(module.public_name("Label#12:34"),"Label")
        for value in ("Version#beta", "#12:34 title", "Label#12:34-extra", "Size#12", "Ticket"):
            self.assertEqual(module.public_name(value),value)

    def test_valid_draft_keeps_literal_suffix(self):
        data={"properties":["Label#12:34","Version#beta"],"exact":["Stable"],"literals":["Ticket#12:34"]}
        self.assertEqual(module.check(data,"`Label`, `Version#beta` = `Stable`; Ticket#12:34."),[])

    def test_leaked_raw_key_is_rejected_even_if_public_key_is_present(self):
        data={"properties":["Label#12:34"],"exact":[],"literals":[]}
        errors=module.check(data,"`Label` has raw key `Label#12:34`.")
        self.assertTrue(any("leaked" in x for x in errors))

    def test_non_numeric_suffix_cannot_be_dropped(self):
        data={"properties":["Version#beta"],"exact":[],"literals":[]}
        self.assertTrue(module.check(data,"`Version`"))

    def test_public_key_substring_in_raw_key_is_not_enough(self):
        data={"properties":["Label#12:34"],"exact":[],"literals":[]}
        errors=module.check(data,"`Label#12:34`")
        self.assertEqual(len(errors),2)

    def test_exact_identifiers_are_case_sensitive(self):
        data={"properties":[],"exact":["Enabled"],"literals":[]}
        self.assertTrue(module.check(data,"`enabled`"))

    def test_literal_that_resembles_a_source_key_is_preserved(self):
        data={"properties":["Label#12:34"],"exact":[],"literals":["Label#12:34"]}
        self.assertEqual(module.check(data,"`Label` displays literal Label#12:34."),[])

    def test_invalid_input_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            p=Path(folder)/"input.json"
            for value in ([],{"properties":"Label"},{"properties":[""]},{"unknown":[]}):
                p.write_text(json.dumps(value))
                with self.assertRaises(ValueError):module.read_spec(p)

if __name__=="__main__":
    unittest.main()
