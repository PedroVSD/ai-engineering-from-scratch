# Limpeza e EDA do Zero

> Dados reais que eu tenho são os que você conserta faltando, duplicadas e tipos antes que o modelo aprenda ou erra.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## Objetivos de aprendizagem

- Detectar e imputar valores ausentes (média, mediana, moda) sem pandas
- Normalizar tipos, remover duplicados e padronizar strings manualmente
- Calculação de correlação de Pearson do zero e montar matriz de correlação
- Gerar um relatório EDA mínimo reproduzível

## O problema

O tempo de um cientista é limpo, estimado em 80% em C.S.V.`""`- Não .`"N/A"`- Não .`"null"`Os modelos não consertam dados em ruínas, mas amplificam.

## O conceito

### Falta: tipos

- MCAR (perda aleatória)  imputar ok.
- MAR (perda depende de outro campo)  imputar condicional.
- O MNAR (perda depende do próprio valor) imputará o seu valor.

Estratégias: remover linha, média/mediana/moda, vizinho mais próximo.

### Correlação de Pearson

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
R = 1 correlação perfeita, 0 nenhuma, -1 inversa.

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

## Construí-lo

### Passo 1: Pesquisar e detectar a falta

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### Passo 2: Imputação

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

### Passo 3: Correlação

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## Usá-lo

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## Envia-o

`outputs/skill-limpeza-eda.md` canalização de limpeza reprodutivel.

## Exercícios

1. Implementar a imputação por grupo (ex: mediana de salário por departamento).
2. Adicione detecção de duplicados por chave composta.
3. Comparar Pearson vs. Spearman em dados com outlier  qual é mais robusto?

## Termos-chave

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## Mais leitura

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
