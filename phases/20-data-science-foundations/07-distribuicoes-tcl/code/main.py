# phases/20-data-science-foundations/07-distribuicoes-tcl/code/main.py
# Lesson: Distribuições e o TCL — docs/en.md
# Spec: Bernoulli/Binomial/Poisson/Normal/Exponencial do zero (math) + simulação TCL

import math
import random


def bernoulli_pmf(k, p):
    if not 0 <= p <= 1:
        raise ValueError("p deve estar em [0,1]")
    if k == 1:
        return p
    if k == 0:
        return 1 - p
    return 0.0


def binom_pmf(k, n, p):
    if not 0 <= p <= 1:
        raise ValueError("p deve estar em [0,1]")
    if not isinstance(n, int) or n < 0:
        raise ValueError("n deve ser inteiro >= 0")
    if not isinstance(k, int) or not 0 <= k <= n:
        return 0.0
    return math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k))


def poisson_pmf(k, lam):
    if lam <= 0:
        raise ValueError("lambda deve ser > 0")
    if not isinstance(k, int) or k < 0:
        return 0.0
    return (lam ** k) * math.exp(-lam) / math.factorial(k)


def normal_pdf(x, mu=0.0, sigma=1.0):
    if sigma <= 0:
        raise ValueError("sigma deve ser > 0")
    return math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (sigma * math.sqrt(2 * math.pi))


def expon_pdf(x, lam):
    if lam <= 0:
        raise ValueError("lambda deve ser > 0")
    return lam * math.exp(-lam * x) if x >= 0 else 0.0


def sample_bernoulli(p, rng):
    return 1 if rng.random() < p else 0


def sample_binomial(n, p, rng):
    return sum(sample_bernoulli(p, rng) for _ in range(n))


def sample_poisson(lam, rng):
    lam_f = float(lam)
    threshold = math.exp(-lam_f)
    k, prod = 0, 1.0
    while True:
        k += 1
        prod *= rng.random()
        if prod <= threshold:
            return k - 1


def sample_expon(lam, rng):
    return -math.log(1 - rng.random()) / lam


def sample_normal(mu, sigma, rng):
    return rng.gauss(mu, sigma)


def sample_means(sampler, n, reps):
    return [sum(sampler() for _ in range(n)) / n for _ in range(reps)]


def mean(data):
    return sum(data) / len(data)


def variance(data):
    m = mean(data)
    return sum((x - m) ** 2 for x in data) / len(data)


def main():
    rng = random.Random(42)
    print("=== Distribuicoes do Zero ===")
    print(f"Binomial P(X=2|n=10,p=.5) = {binom_pmf(2, 10, 0.5):.4f}")
    print(f"Poisson  P(X=3|lam=2)      = {poisson_pmf(3, 2.0):.4f}")
    print(f"Normal   f(0|0,1)         = {normal_pdf(0):.4f}")
    print(f"Expon    f(1|lam=1)       = {expon_pdf(1, 1.0):.4f}")

    # Validação amostral: binomial(10, .5) -> E=5, Var=2.5
    draws = [sample_binomial(10, 0.5, rng) for _ in range(20_000)]
    print(f"binomial amostral: media={mean(draws):.3f} (->5.0) var={variance(draws):.3f} (->2.5)")

    # TCL: base exponencial (assimétrica!) -> médias ~ N(1, 1/30)
    rng2 = random.Random(7)
    means = sample_means(lambda: sample_expon(1.0, rng2), n=30, reps=2000)
    print(f"TCL exp(1) n=30: E[Xbar]={mean(means):.3f} (->1.0) Var={variance(means):.4f} (->0.0333)")

    try:
        import numpy as np
        r = np.random.default_rng(0)
        s = r.binomial(10, 0.5, size=50_000)
        print(f"[numpy] binomial: media={s.mean():.3f} var={s.var():.3f}")
        e = r.exponential(1.0, size=(2000, 30)).mean(axis=1)
        print(f"[numpy] TCL exp: E[Xbar]={e.mean():.3f} Var={e.var():.4f}")
    except ImportError:
        print("numpy não instalado — comparação pulada (pip install numpy)")

    print("OK — distribuicoes + TCL validados.")


if __name__ == "__main__":
    main()
