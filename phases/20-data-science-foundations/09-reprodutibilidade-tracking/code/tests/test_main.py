import json
import random
import unittest
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m


class TestReproTracking(unittest.TestCase):
    def test_split_deterministic_same_seed(self):
        a_train, a_test = m.train_test_split(m.DATASET, seed=42)
        b_train, b_test = m.train_test_split(m.DATASET, seed=42)
        self.assertEqual(a_train, b_train)
        self.assertEqual(a_test, b_test)

    def test_split_differs_other_seed(self):
        a_train, _ = m.train_test_split(m.DATASET, seed=42)
        b_train, _ = m.train_test_split(m.DATASET, seed=7)
        self.assertNotEqual(a_train, b_train)

    def test_dataset_hash_stable_and_sensitive(self):
        h1 = m.dataset_hash(m.DATASET)
        h2 = m.dataset_hash([dict(r) for r in m.DATASET])
        self.assertEqual(h1, h2)
        changed = [dict(r) for r in m.DATASET]
        changed[0] = {**changed[0], "y": 9999}
        self.assertNotEqual(h1, m.dataset_hash(changed))

    def test_set_seed_repeats_sequence(self):
        m.set_seed(123)
        a = [random.random() for _ in range(3)]
        m.set_seed(123)
        b = [random.random() for _ in range(3)]
        self.assertEqual(a, b)

    def test_log_load_roundtrip(self):
        with tempfile.TemporaryDirectory() as d:
            p = str(Path(d) / "runs.jsonl")
            m.log_run(p, {"lr": 0.01}, {"mae": 1.5}, seed=42, dhash="abc")
            m.log_run(p, {"lr": 0.02}, {"mae": 1.0}, seed=42, dhash="abc")
            runs = m.load_runs(p)
            self.assertEqual(len(runs), 2)
            self.assertEqual(runs[0]["params"], {"lr": 0.01})

    def test_best_run_picks_min_mae(self):
        runs = [
            {"metrics": {"mae": 2.0}, "params": {}},
            {"metrics": {"mae": 0.5}, "params": {}},
        ]
        self.assertEqual(m.best_run(runs, "mae")["metrics"]["mae"], 0.5)

    def test_run_experiment_logs_hash_and_seed(self):
        with tempfile.TemporaryDirectory() as d:
            p = str(Path(d) / "runs.jsonl")
            rec = m.run_experiment(m.DATASET, seed=42, test_ratio=0.2, path=p)
            self.assertEqual(rec["seed"], 42)
            self.assertEqual(rec["dataset_hash"], m.dataset_hash(m.DATASET))
            self.assertIn("mae", rec["metrics"])


if __name__ == "__main__":
    unittest.main()
