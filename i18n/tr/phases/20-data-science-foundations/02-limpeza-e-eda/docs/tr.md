# Limpeza e EDA do Zero

> Gerçek bilgi kayıp olduğunu gösterir, modelin yanlışını öğrenmesinden önce kopyalar ve türler vardır.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## Öğrenme Hedefleri

- Pandas olarak belirlenmiş değerleri (medya, mediana, moda) tespit etmek
- Normalleştirme tipleri, kopyaları kaldırma ve ipleri manuel olarak düzenle
- Pearson'un hesaplama korelasyonı sıfır ve montar korelasyon matrisi
- Gerar um relatório EDA mínimo reproduzível

## Sorun

Bir bilim adamı tempounun %80'ini temizlemesi için tahmin ediliyor.`""`- Evet .`"N/A"`- Evet .`"null"`Bu yüzden, bu modellerin kalıntıları daha da artıyor.

## Anlaşım

### Kaybolan: tipler

- MCAR (perda aleatória)  imputar ok.
- MAR (perda depende de outro campo)  imputar condicional.
- MNAR (kırıklık kendi cesaretine bağlı) 

Stratejiler: liniye çıkartmak, media/mediana/moda, vizinho mais próximo.

### Pearson'ın ilişkisi

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
r=1 correlação perfeita, 0 nenhuma, -1 inversa.

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

## Yapın

### Adım 1: Kayıpları araştırmak ve tespit etmek

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### Adım 2: Imputação

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

### Adım 3: Korrelação

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## Kullan

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## Gönder

`outputs/skill-limpeza-eda.md` üretilebilir bir boru hattı.

## Egzersizler

1. Grup başına imputação (örneğin, ortalama maaş per departamento) uygulanır.
2. Ayrıca, kompostadan kopyalar tespit edilmiştir.
3. Pearson vs. Spearman'ı karşılaştırın. En sağlamsı hangisi?

## Anahtar Terimler

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## Daha Fazla Okumak

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
