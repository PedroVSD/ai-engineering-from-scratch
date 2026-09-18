import unittest
import math
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m


class TestDescritiva(unittest.TestCase):
    def test_mean(self):
        self.assertAlmostEqual(m.mean([1,2,3,4,5]), 3.0)

    def test_median_odd_even(self):
        self.assertEqual(m.median([3,1,2]), 2)
        self.assertEqual(m.median([1,2,3,4]), 2.5)

    def test_std_variance(self):
        data = [2,4,4,4,5,5,7,9]
        self.assertAlmostEqual(m.mean(data), 5.0)
        self.assertAlmostEqual(m.variance(data), 4.0)
        self.assertAlmostEqual(m.std(data), 2.0)

    def test_quartiles_iqr(self):
        data = [1,2,3,4,5,6,7,8]
        q1, q2, q3 = m.quartiles(data)
        self.assertAlmostEqual(q2, 4.5)
        self.assertGreater(m.iqr(data), 0)

    def test_outliers_iqr(self):
        data = [10,12,14,15,18,20,100]
        out = m.detect_outliers_iqr(data)
        self.assertIn(100, out)
        self.assertNotIn(14, out)

    def test_z_scores(self):
        data = [0,0,0,10]
        zs = m.z_scores(data)
        self.assertAlmostEqual(sum(zs), 0, places=6)

    def test_histogram_counts(self):
        self.assertEqual(sum(m.histogram_counts([1,2,3,4,5], bins=2)), 5)


if __name__ == "__main__":
    unittest.main()
