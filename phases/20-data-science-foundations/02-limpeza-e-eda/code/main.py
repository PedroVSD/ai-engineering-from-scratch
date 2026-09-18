# phases/20-data-science-foundations/02-limpeza-e-eda/code/main.py
# Lesson: Limpeza e EDA do Zero

import math
import csv
import io


def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")


def parse_csv(text):
    reader = csv.DictReader(io.StringIO(text))
    return list(reader)


def impute(rows, col, strategy="median"):
    vals = []
    for r in rows:
        if not is_missing(r[col]):
            try:
                vals.append(float(r[col]))
            except ValueError:
                pass
    if not vals:
        return None
    vals.sort()
    if strategy == "mean":
        fill = sum(vals) / len(vals)
    elif strategy == "median":
        n = len(vals)
        fill = vals[n // 2] if n % 2 == 1 else (vals[n // 2 - 1] + vals[n // 2]) / 2
    else:
        fill = max(set(vals), key=vals.count)
    for r in rows:
        if is_missing(r[col]):
            r[col] = fill
    return fill


def deduplicate(rows, key=None):
    seen = set()
    out = []
    for r in rows:
        k = tuple(r[c] for c in key) if key else tuple(sorted(r.items()))
        if k not in seen:
            seen.add(k)
            out.append(r)
    return out


def pearson(x, y):
    mx = sum(x) / len(x)
    my = sum(y) / len(y)
    num = sum((a - mx) * (b - my) for a, b in zip(x, y))
    den = (sum((a - mx) ** 2 for a in x) * sum((b - my) ** 2 for b in y)) ** 0.5
    return num / den if den else 0


def correlation_matrix(data):
    cols = list(data.keys())
    mat = {}
    for c1 in cols:
        for c2 in cols:
            mat[(c1, c2)] = pearson(data[c1], data[c2])
    return mat


def main():
    csv_text = """nome,idade,salario,dept
Ana,28,5000,eng
Bruno,,6000,eng
Carlos,35,N/A,mkt
Ana,28,5000,eng
Diana,30,8000,eng
"""
    rows = parse_csv(csv_text)
    print(f"linhas brutas: {len(rows)}")
    rows = deduplicate(rows, key=["nome", "idade", "salario"])
    print(f"após dedup: {len(rows)}")
    fill = impute(rows, "idade", "median")
    print(f"imputação idade mediana={fill}")
    impute(rows, "salario", "median")
    print("linhas limpas:", rows)

    x = [float(r["idade"]) for r in rows]
    y = [float(r["salario"]) for r in rows]
    print(f"Pearson idade×salário: {pearson(x,y):.3f}")

    mat = correlation_matrix({"idade": x, "salario": y})
    print(f"matriz: {mat}")

    try:
        import pandas as pd
        df = pd.read_csv(io.StringIO(csv_text), na_values=["", "N/A", "null"])
        print("[pandas] missing por coluna:\n", df.isna().sum().to_dict())
    except ImportError:
        print("pandas não instalado — pulado")

    print("OK — limpeza e EDA validado.")


if __name__ == "__main__":
    main()
