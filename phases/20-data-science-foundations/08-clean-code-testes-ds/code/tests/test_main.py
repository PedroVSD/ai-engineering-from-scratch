import copy
import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m


class TestCleanCodeDS(unittest.TestCase):
    def test_validate_schema_ok(self):
        rows = [{"nome": "ana", "idade": 30, "salario": 5000.0}]
        self.assertEqual(m.validate_schema(rows, m.SCHEMA), [])

    def test_validate_schema_missing_and_bad_type(self):
        rows = [{"nome": "ana", "idade": "trinta"}]
        errors = m.validate_schema(rows, m.SCHEMA)
        self.assertTrue(any("salario" in e for e in errors))
        self.assertTrue(any("idade" in e for e in errors))

    def test_clean_rows_coerces_and_drops_negatives(self):
        rows = [
            {"nome": " bruno ", "idade": "25", "salario": "4200.5"},
            {"nome": "x", "idade": -1, "salario": 10.0},
            {"nome": "y", "idade": 20, "salario": -5.0},
        ]
        out = m.clean_rows(rows)
        self.assertEqual(len(out), 1)
        self.assertEqual(out[0]["nome"], "bruno")
        self.assertEqual(out[0]["idade"], 25)

    def test_pure_functions_do_not_mutate(self):
        rows = [{"nome": "ana", "idade": 30, "salario": 5000.0}]
        snapshot = copy.deepcopy(rows)
        m.clean_rows(rows)
        m.featurize(rows)
        self.assertEqual(rows, snapshot)

    def test_featurize_adulto_flag(self):
        out = m.featurize([
            {"nome": "a", "idade": 17, "salario": 1.0},
            {"nome": "b", "idade": 18, "salario": 1.0},
        ])
        self.assertFalse(out[0]["adulto"])
        self.assertTrue(out[1]["adulto"])

    def test_check_quality_detects_duplicates(self):
        rows = [
            {"nome": "ana", "idade": 30, "salario": 1.0},
            {"nome": "ana", "idade": 30, "salario": 2.0},
        ]
        self.assertFalse(m.check_quality(rows)["sem_duplicatas"])

    def test_run_pipeline_raises_on_bad_schema(self):
        with self.assertRaises(ValueError):
            m.run_pipeline([{"nome": "ana"}])


if __name__ == "__main__":
    unittest.main()
