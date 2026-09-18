import unittest
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m


class TestProbabilidade(unittest.TestCase):
    def test_cond_prob(self):
        self.assertAlmostEqual(m.cond_prob(1 / 6, 3 / 6), 1 / 3)

    def test_cond_prob_invalid(self):
        with self.assertRaises(ValueError):
            m.cond_prob(0.1, 0)

    def test_independence(self):
        self.assertTrue(m.is_independent(0.5, 0.5, 0.25))
        self.assertFalse(m.is_independent(0.5, 0.5, 0.30))
        self.assertAlmostEqual(m.joint_if_independent(0.2, 0.3), 0.06)

    def test_total_prob(self):
        self.assertAlmostEqual(m.total_prob([0.99, 0.05], [0.001, 0.999]), 0.05094)
        with self.assertRaises(ValueError):
            m.total_prob([0.5], [0.4])  # priors não somam 1

    def test_bayes_medical(self):
        p_pos = m.total_prob([0.99, 0.05], [0.001, 0.999])
        post = m.bayes(0.99, 0.001, p_pos)
        self.assertAlmostEqual(post, 0.0194, places=3)
        with self.assertRaises(ValueError):
            m.bayes(0.5, 0.5, 0)

    def test_pmf_moments(self):
        dado = m.pmf([1, 2, 3, 4, 5, 6], [1 / 6] * 6)
        self.assertAlmostEqual(sum(dado.values()), 1.0)
        self.assertAlmostEqual(m.expected_value(dado), 3.5)
        self.assertAlmostEqual(m.variance_dist(dado), 35 / 12)
        with self.assertRaises(ValueError):
            m.pmf([1, 2], [0.5, 0.4])  # não soma 1


if __name__ == "__main__":
    unittest.main()
