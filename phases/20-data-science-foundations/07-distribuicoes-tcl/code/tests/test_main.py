import unittest
import math
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m


class TestDistribuicoes(unittest.TestCase):
    def test_bernoulli(self):
        self.assertAlmostEqual(m.bernoulli_pmf(1, 0.3), 0.3)
        self.assertAlmostEqual(m.bernoulli_pmf(0, 0.3), 0.7)
        self.assertEqual(m.bernoulli_pmf(2, 0.3), 0.0)
        with self.assertRaises(ValueError):
            m.bernoulli_pmf(1, 1.5)

    def test_binom_pmf(self):
        self.assertAlmostEqual(m.binom_pmf(2, 10, 0.5), 45 / 1024)
        self.assertAlmostEqual(sum(m.binom_pmf(k, 10, 0.5) for k in range(11)), 1.0)
        self.assertEqual(m.binom_pmf(11, 10, 0.5), 0.0)

    def test_poisson_pmf(self):
        self.assertAlmostEqual(m.poisson_pmf(3, 2.0), 0.1804470443)
        self.assertAlmostEqual(sum(m.poisson_pmf(k, 2.0) for k in range(15)), 1.0, places=5)
        with self.assertRaises(ValueError):
            m.poisson_pmf(1, 0)

    def test_normal_expon_pdf(self):
        self.assertAlmostEqual(m.normal_pdf(0), 1 / math.sqrt(2 * math.pi))
        self.assertAlmostEqual(m.expon_pdf(0, 1.0), 1.0)
        self.assertEqual(m.expon_pdf(-1, 1.0), 0.0)
        with self.assertRaises(ValueError):
            m.normal_pdf(0, sigma=0)

    def test_sampling_moments(self):
        rng = random.Random(0)
        draws = [m.sample_binomial(10, 0.5, rng) for _ in range(5000)]
        self.assertAlmostEqual(sum(draws) / len(draws), 5.0, delta=0.15)

    def test_tcl_mean_converges(self):
        rng = random.Random(1)
        means = m.sample_means(lambda: m.sample_expon(1.0, rng), n=30, reps=500)
        avg = sum(means) / len(means)
        var = sum((x - avg) ** 2 for x in means) / len(means)
        self.assertAlmostEqual(avg, 1.0, delta=0.1)
        self.assertAlmostEqual(var, 1 / 30, delta=0.02)


if __name__ == "__main__":
    unittest.main()
