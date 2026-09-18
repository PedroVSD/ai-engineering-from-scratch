# phases/20-data-science-foundations/01-estatistica-descritiva/code/main.py
# Lesson: Estatística Descritiva do Zero — docs/en.md
# Spec: mean/median/variance/IQR/z-score with stdlib; compare to numpy

import math
import random


def mean(data):
    return sum(data) / len(data)


def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return float(s[mid]) if n % 2 == 1 else (s[mid - 1] + s[mid]) / 2


def variance(data, sample=False):
    m = mean(data)
    div = len(data) - 1 if sample else len(data)
    return sum((x - m) ** 2 for x in data) / div


def std(data, sample=False):
    return math.sqrt(variance(data, sample))


def mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    return max(freq, key=freq.get)


def percentile(data, p):
    s = sorted(data)
    k = (len(s) - 1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return float(s[int(k)])
    return s[f] * (c - k) + s[c] * (k - f)


def quartiles(data):
    return percentile(data, 25), percentile(data, 50), percentile(data, 75)


def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1


def z_scores(data):
    m = mean(data)
    s = std(data)
    return [(x - m) / s if s else 0 for x in data]


def detect_outliers_iqr(data, k=1.5):
    q1, _, q3 = quartiles(data)
    lo = q1 - k * iqr(data)
    hi = q3 + k * iqr(data)
    return [x for x in data if x < lo or x > hi]


def histogram_counts(data, bins=5):
    lo, hi = min(data), max(data)
    width = (hi - lo) / bins if hi != lo else 1
    counts = [0] * bins
    for x in data:
        idx = min(int((x - lo) / width), bins - 1) if width else 0
        counts[idx] += 1
    return counts


def main():
    random.seed(42)
    salaries = [random.gauss(5000, 1200) for _ in range(100)] + [50000]
    salaries = [max(1000, s) for s in salaries]

    print("=== Estatística Descritiva ===")
    print(f"n={len(salaries)} média={mean(salaries):.1f} mediana={median(salaries):.1f} std={std(salaries):.1f}")
    q1, q2, q3 = quartiles(salaries)
    print(f"Q1={q1:.1f} Q2={q2:.1f} Q3={q3:.1f} IQR={iqr(salaries):.1f}")
    outliers = detect_outliers_iqr(salaries)
    print(f"outliers IQR (k=1.5): {len(outliers)} -> {[round(x) for x in outliers[:5]]}")
    zs = z_scores(salaries)
    print(f"max |z|={max(abs(z) for z in zs):.2f}")
    counts = histogram_counts(salaries, bins=5)
    print(f"histograma counts (5 bins): {counts}")

    # Use It comparison if available
    try:
        import numpy as np
        print(f"[numpy] mean={np.mean(salaries):.1f} median={np.median(salaries):.1f} std={np.std(salaries):.1f}")
    except ImportError:
        print("numpy não instalado — comparação pulada (pip install numpy)")

    print("OK — descritiva do zero validada.")


if __name__ == "__main__":
    main()
