# Limpeza e EDA hacer cero

> Los datos que realmente me faltan se conservan, se duplican y se producen antes de que el modelo aprenda o se equivoque.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## Objetivos de aprendizaje

- Detectar y imputar valores ausentes (media, mediana, moda) sem pandas
- Normaliza tipos, elimina duplicadas y padroniza las cuerdas manualmente
- Calculación de correlación de Pearson hacer cero y montar matriz de correlación
- Gerar um relatório EDA mínimo reproducible

## El problema

Se estima que el 80% del tiempo de un científico es limpio.`""`¿ Qué ?`"N/A"`¿ Qué ?`"null"`Los modelos no consertan en las ruinas y se amplifican.

## El concepto

### Desaparecido: tipos

- MCAR (perda aleatória)  imputar ok.
- MAR (perda depende de otro campo)  imputar condicional.
- El MNAR (perda depende del propio valor)  imputar viesado.

Estrategias: remover linha, media/mediana/moda, vizinho mais próximo.

### Correlación de Pearson

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
R = 1 correlación perfecta, 0 ninguna, -1 inversa.

```mermaid
flowchart LR
    A[CSV bruto] --> B[Parse tipos]
    B --> C[Missing?]
    C --> D[Imputar / Remover]
    D --> E[Duplicatas]
    E --> F[Padronizar]
    F --> G[Correlação]
    G --> H[Relatório EDA]
```

```figure
eda-pipeline
```

## Construye el mismo

### Paso 1: Revisar y detectar la falta

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### Paso 2: Imputación

```python
def impute(rows, col, strategy="median"):
    vals = [float(r[col]) for r in rows if not is_missing(r[col])]
    vals.sort()
    if strategy == "mean":
        fill = sum(vals)/len(vals)
    elif strategy == "median":
        fill = vals[len(vals)//2]
    else: # mode
        fill = max(set(vals), key=vals.count)
    for r in rows:
        if is_missing(r[col]):
            r[col] = fill
    return fill
```

### Paso 3: Correlación

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## Usalo

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## Envío

`outputs/skill-limpeza-eda.md` tubería de limpeza reproducible.

## Los ejercicios

1. Implementar la imputación por grupo (ex: mediana de salario por departamento).
2. Adicione detección de duplicados por composta clave.
3. Comparar Pearson vs. Spearman en datos de com outlier ¿Cuál es el más robusto?

## Términos clave

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## Leer más

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
