# Statística Descritiva do Zero

> Mediana e variância, bir tablo tarafından gizlenen bir tarih anlatır.

**Type:** Build
**Languages:** Python
**Prerequisites:** None
**Time:** ~60 minutes

## Öğrenme Hedefleri

- Calculara media, mediana, moda, variância, desvio-padrão e quartis usando apenas stdlib
- Matplotlib kullanmadan önce bir tarih programı ve kutu planı oluşturun
- IQR ve z-score ile belirsiz değerleri tespit etmek ve her zaman yanlış olduğunu açıklamak
- Bir empirici dağılımı normal ve yorumlayıcı asimetri ile kıyasla

## Sorun

10.000 ücretle CSV alıyorsunuz.$ 8.500, mas 70% das pessoas ganham menos que isso. Por quê? Um único CEO com R$Eğer sadece bir medya raporunu yaparsanız, ben de istiyorum.

Veriler biliminde verileri bir metrika olarak özetlemek sadece en yaygın ve en pahalı hata.

## Anlaşım

### Centro: media vs mediana vs moda

```
dados = [2, 3, 3, 5, 500]
média   = (2+3+3+5+500)/5 = 102.6  <- sensível a outlier
mediana = valor do meio ordenado = 3  <- robusta
moda    = valor mais frequente = 3
```

Kural: simetrik dağıtım -> media ~= mediana.

### Dispersão: variância e desvio-padrão

```
variância = média((x - média)^2)
desvio    = sqrt(variância)
```

Desvio responde: "em media, quanto cada ponto se afasta do centro?" grupları karşılaştırmak için kullanılır.

### Quartis e IQR (robusto)

Doluların sırası. Q1 = yüzde 25, Q2 = ortalama, Q3 = yüzde 75.
IQR = Q3 - Q1 (% 50 merkezli amplitud).

Regra de Tukey'nin dışa çıkışlılıkları:
```
limite_inf = Q1 - 1.5*IQR
limite_sup = Q3 + 1.5*IQR
```

### Z puanı (parametrik)

```
z = (x - média) / desvio
```
|z| > 3 = candidato a outlier, mas assume distribuição ~normal. Em dados assimétricos, IQR é melhor.

```mermaid
flowchart LR
    A[Dados brutos] --> B[Ordenar]
    B --> C[Centro: média/mediana]
    B --> D[Dispersão: var/desvio]
    B --> E[Forma: histograma]
    E --> F{Assimétrica?}
    F -->|Sim| G[Use mediana + IQR]
    F -->|Não| H[Use média + desvio]
```

```figure
stats-descriptive-overview
```

## Yapın

### Adım 1: Statísticas centrais e dispersão do zero

```python
import math

def mean(data):
    return sum(data) / len(data)

def median(data):
    s = sorted(data)
    n = len(s)
    mid = n // 2
    return s[mid] if n % 2 == 1 else (s[mid-1] + s[mid]) / 2

def variance(data, sample=False):
    m = mean(data)
    div = len(data) - 1 if sample else len(data)
    return sum((x - m)**2 for x in data) / div

def std(data, sample=False):
    return math.sqrt(variance(data, sample))

def mode(data):
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    return max(freq, key=freq.get)

data = [2, 3, 3, 5, 500]
print(f"média={mean(data):.1f} mediana={median(data)} moda={mode(data)} std={std(data):.1f}")
```

### Adım 2: Quartis e IQR

```python
def percentile(data, p):
    s = sorted(data)
    k = (len(s)-1) * p / 100
    f = math.floor(k)
    c = math.ceil(k)
    if f == c:
        return s[int(k)]
    return s[f] * (c - k) + s[c] * (k - f)

def quartiles(data):
    return percentile(data, 25), percentile(data, 50), percentile(data, 75)

def iqr(data):
    q1, _, q3 = quartiles(data)
    return q3 - q1

q1, q2, q3 = quartiles([1,2,3,4,5,6,7,8,9,100])
print(f"Q1={q1} Q2={q2} Q3={q3} IQR={iqr([1,2,3,4,5,6,7,8,9,100])}")
# outlier: 100 > Q3+1.5*IQR ?
```

### Adım 3: Histogram ASCII

```python
def histogram(data, bins=5):
    lo, hi = min(data), max(data)
    width = (hi - lo) / bins
    counts = [0]*bins
    for x in data:
        idx = min(int((x - lo) / width), bins-1) if width else 0
        counts[idx] += 1
    for i, c in enumerate(counts):
        bar = "#" * c
        print(f"{lo + i*width:6.1f} | {bar} ({c})")

histogram([1,1,2,2,2,3,3,5,8,9], bins=4)
```

## Kullan

Hatta hesaplama`numpy`- Ne ?`statistics`- ...

```python
import statistics
import numpy as np

data = [2, 3, 3, 5, 500]
print(statistics.mean(data), statistics.median(data), statistics.stdev(data))
print(np.mean(data), np.median(data), np.std(data, ddof=0))
print(np.percentile(data, [25,50,75]))
# histograma real
# import matplotlib.pyplot as plt
# plt.hist(data, bins=10); plt.show()
```

Kodu sıfır ve numpy bir ikiinci evin onluk biriminde toplanmalıdır.

## Gönder

Artefato:`outputs/skill-estatistica-descritiva.md` Tüm EDA'nın kontrol listesinde: "antes de training, reporte média/mediana, desvio/IQR, histogram e % de outliers".

## Egzersizler

1. Gere 1000 gösterge`exp(λ=1)`Medya ile mediana karşılaştırmak.
2. Asimetriyi uygulayın (skew) = E[(x-média) ^3]/desvio^3 sem libs.
3. Bir IQR kuralını değiştirin 1.5 ile 3.0. kaç kaç değer kaybediyorsun?

## Anahtar Terimler

| Term | O que dizem | O que realmente é |
|---|---|---|
| Média | "valor típico" | Soma/n, sensível a outliers; só típica se distribuição simétrica |
| Mediana | "meio dos dados" | Valor que corta 50% abaixo/acima; robusta |
| Desvio-padrão | "erro médio" | Raiz da variância; distância típica até a média |
| IQR | "caixa do boxplot" | Q3-Q1; amplitude dos 50% centrais |
| Z-score | "quantos desvios" | (x-média)/desvio; assume normalidade |
| Outlier | "ponto estranho" | Observação além de Q3+1.5*IQR ou |z|>3 |

## Daha Fazla Okumak

- [Seeing Theory — Descriptive Stats](https://seeing-theory.brown.edu/) visual interativo
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/)Referans
- [SciPy stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) para üretim
