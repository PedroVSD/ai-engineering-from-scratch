# phases/20-data-science-foundations/06-probabilidade-fundamentos/code/main.py
# Lesson: Probabilidade do Zero — docs/en.md
# Spec: condicional/independência/total/Bayes + PMF/esperança/variância em stdlib

import math


def cond_prob(p_ab, p_b):
    if p_b <= 0:
        raise ValueError("P(B) deve ser > 0")
    return p_ab / p_b


def joint_if_independent(p_a, p_b):
    return p_a * p_b


def is_independent(p_a, p_b, p_ab, tol=1e-9):
    return abs(p_ab - p_a * p_b) <= tol


def total_prob(cond_probs, priors):
    if len(cond_probs) != len(priors):
        raise ValueError("listas devem ter o mesmo tamanho")
    if abs(sum(priors) - 1.0) > 1e-9:
        raise ValueError("priors devem somar 1")
    return sum(c * p for c, p in zip(cond_probs, priors))


def bayes(p_a_given_b, p_b, p_a):
    if p_a <= 0:
        raise ValueError("P(A) deve ser > 0")
    return p_a_given_b * p_b / p_a


def pmf(values, probs):
    if len(values) != len(probs):
        raise ValueError("values e probs devem ter o mesmo tamanho")
    if any(p < 0 for p in probs):
        raise ValueError("probabilidades não podem ser negativas")
    if abs(sum(probs) - 1.0) > 1e-9:
        raise ValueError("probs devem somar 1")
    return dict(zip(values, probs))


def expected_value(dist):
    return sum(x * p for x, p in dist.items())


def variance_dist(dist):
    mu = expected_value(dist)
    return sum(((x - mu) ** 2) * p for x, p in dist.items())


def std_dist(dist):
    return math.sqrt(variance_dist(dist))


def main():
    print("=== Probabilidade do Zero ===")
    print(f"P(6|par) = {cond_prob(1 / 6, 3 / 6):.3f}")
    print(f"moedas independentes? {is_independent(0.5, 0.5, 0.25)}")

    # Caso canônico: teste médico (sens=0.99, espec=0.95, prev=0.001)
    p_pos = total_prob([0.99, 0.05], [0.001, 0.999])
    print(f"P(positivo) = {p_pos:.4f}")
    print(f"P(doente|positivo) = {bayes(0.99, 0.001, p_pos):.4f} (~2%, não 99%)")

    dado = pmf([1, 2, 3, 4, 5, 6], [1 / 6] * 6)
    print(f"dado: E[X]={expected_value(dado):.2f} Var={variance_dist(dado):.4f} std={std_dist(dado):.4f}")

    # Use It: conferência empírica via simulação
    try:
        import random
        random.seed(0)
        n = 200_000
        dp = sum(1 for _ in range(n)
                 if random.random() < 0.001 and random.random() < 0.99)
        sp = sum(1 for _ in range(n)
                 if random.random() >= 0.001 and random.random() < 0.05)
        print(f"[simulacao n={n}] P(doente|+) ~= {dp / (dp + sp):.4f}")
    except ImportError:  # pragma: no cover
        print("random indisponível — simulação pulada")

    print("OK — probabilidade do zero validada.")


if __name__ == "__main__":
    main()
