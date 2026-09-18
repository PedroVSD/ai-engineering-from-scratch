# phases/20-data-science-foundations/08-clean-code-testes-ds/code/main.py
# Lesson: Clean Code e Testes para Data Science — docs/en.md
# Spec: pure-function pipeline, list-of-dicts schema validation, data-quality checks (stdlib only)

RAW_ROWS = [
    {"nome": "ana", "idade": 30, "salario": 5000.0},
    {"nome": " bruno ", "idade": "25", "salario": "4200.5"},
    {"nome": "cati", "idade": 17, "salario": 1500.0},
    {"nome": "dan", "idade": -3, "salario": 3000.0},
    {"nome": "eli", "idade": 41, "salario": -100.0},
]

SCHEMA = {"nome": str, "idade": int, "salario": float}


def validate_schema(rows, schema):
    """Return list of error strings; empty means valid. Pure, no mutation."""
    errors = []
    for i, row in enumerate(rows):
        for col, tipo in schema.items():
            if col not in row:
                errors.append(f"linha {i}: coluna ausente '{col}'")
                continue
            try:
                tipo(row[col])
            except (ValueError, TypeError):
                errors.append(
                    f"linha {i}: '{col}'={row[col]!r} nao converte para {tipo.__name__}"
                )
    return errors


def clean_rows(rows):
    """Strip names, coerce types, drop negative idade/salario. Returns new list."""
    out = []
    for r in rows:
        novo = {
            "nome": str(r["nome"]).strip(),
            "idade": int(r["idade"]),
            "salario": float(r["salario"]),
        }
        if novo["idade"] >= 0 and novo["salario"] >= 0:
            out.append(novo)
    return out


def featurize(rows):
    """Add derived column 'adulto'. Returns new list, input untouched."""
    return [{**r, "adulto": r["idade"] >= 18} for r in rows]


def check_quality(rows):
    """Named data-quality invariants. Returns dict of bool."""
    nomes_idades = [(r.get("nome"), r.get("idade")) for r in rows]
    return {
        "sem_nulos": all(v is not None and v != "" for r in rows for v in r.values()),
        "idades_validas": all(
            isinstance(r.get("idade"), int) and 0 <= r["idade"] <= 120 for r in rows
        ),
        "salarios_nao_negativos": all(
            isinstance(r.get("salario"), (int, float)) and r["salario"] >= 0
            for r in rows
        ),
        "sem_duplicatas": len(set(nomes_idades)) == len(rows),
    }


def run_pipeline(rows):
    """Validate on the edge, then clean + featurize. Raises ValueError on bad schema."""
    errors = validate_schema(rows, SCHEMA)
    if errors:
        raise ValueError("schema invalido:\n" + "\n".join(errors[:5]))
    return featurize(clean_rows(rows))


def main():
    print("=== Clean Code + Testes DS ===")
    errors = validate_schema(RAW_ROWS, SCHEMA)
    print(f"schema errors nas brutas: {len(errors)}")
    for e in errors[:5]:
        print(f"  - {e}")
    result = run_pipeline(RAW_ROWS)
    print(f"linhas brutas={len(RAW_ROWS)} limpas={len(result)}")
    for r in result:
        print(f"  {r}")
    quality = check_quality(result)
    print(f"quality: {quality}")
    print("OK — pipeline modular validado.")


if __name__ == "__main__":
    main()
