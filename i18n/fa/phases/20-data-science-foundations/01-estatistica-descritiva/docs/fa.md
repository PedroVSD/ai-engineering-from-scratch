# Statística Descritiva do Zero

> میدیا، میدیانا و ویرینسیا یک تاریخ را روایت می کند که یک جدول پنهان می کند تا یک پاندا را کشف کند.

**Type:** Build
**Languages:** Python
**Prerequisites:** None
**Time:** ~60 minutes

## اهداف یادگیری

- محاسبه رسانه، متوسط، مد، ویرینسی، رفتار و رفتار با استفاده از فقط stdlib
- ساخت یک برنامه تاریخی و نقشه ی جعبه ای قبل از استفاده از نقشه ی ساز
- تشخیص تفاوت های خارق العاده با IQR و Z-score و توضیح دادن زمانی که هر یک از آنها اشتباه می کنند
- مقایسه یک توزیع تجربی با یک تعبیر طبیعی و مختص

## مشکل

شما یک CSV با 10 هزار تنفع دریافت می کنید.$ 8.500, mas 70% das pessoas ganham menos que isso. Por quê? Um único CEO com R$500 هزار تا ميديا رو ميگي اگه فقط ميديا رو گزارش کني، ميخواي بدونم

در علوم داده، خلاصه داده ها به عنوان یک متریک تنها یک اشتباه رایج و گرانبها است. قبل از هر مدل، شما باید توصیف کنید: کجا در مرکز است، چقدر داده ها به طور گسترده، چگونه یک شکل توزیع است. به همین ترتیب، بازگشت و یادگیری عمیق به صورت جعبه-پریتا.

## مفهوم

### مرکز: رسانه در مقابل مدانا در مقابل مدا

```
dados = [2, 3, 3, 5, 500]
média   = (2+3+3+5+500)/5 = 102.6  <- sensível a outlier
mediana = valor do meio ordenado = 3  <- robusta
moda    = valor mais frequente = 3
```

اصول: توزیع simétrica -> média ~= mediana. Assimétrica à direita -> média > mediana (سوال های شغلی).

### پخش: variância e desvio-padrão

```
variância = média((x - média)^2)
desvio    = sqrt(variância)
```

پاسخ: "در رسانه ها، هر نقطه چقدر از مرکز فاصله دارد؟"

### کوارتس و IQR (روبوست)

اردنوس داده ها. Q1 = پرسنلت 25، Q2 = متوسط، Q3 = پرسنلت 75
IQR = Q3 - Q1 (امپلیتوس 50٪ مرکز)

قوانین دو تیکی برای موارد غیر معمول:
```
limite_inf = Q1 - 1.5*IQR
limite_sup = Q3 + 1.5*IQR
```

### نمره Z (پارا متریک)

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

## آن را بسازید

### مرحله ی اول: مرکز های آماری و انتشار صفر

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

### مرحله دوم: کوارتس و IQR

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

### مرحله سوم: هیستوگراما ASCII

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

## ازش استفاده کن

حتی محاسبه`numpy`-بله .`statistics`:

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

کد شما باید صفر و عدد دو را با یک عدد دو برابر کند.

## -باده

آرتیفاتو:`outputs/skill-estatistica-descritiva.md` چک لیست برای تمام EDA: "antes de train, reporte média/mediana, desvio/IQR, histogram e % de outliers".

## تمرینات

1. ۱۰۰۰ نمونه برداری`exp(λ=1)`و مقایسه رسانه با رسانه. چرا تفاوت می کنیم؟
2. تطبیق اسیمتری (skew) = E[(x-média) ^3]/desvio^3 sem libs. تست آنها داده های simétricos vs assimétricos.
3. چند تا از اونها رو که از دست دادي؟

## اصطلاحات کلیدی

| Term | O que dizem | O que realmente é |
|---|---|---|
| Média | "valor típico" | Soma/n, sensível a outliers; só típica se distribuição simétrica |
| Mediana | "meio dos dados" | Valor que corta 50% abaixo/acima; robusta |
| Desvio-padrão | "erro médio" | Raiz da variância; distância típica até a média |
| IQR | "caixa do boxplot" | Q3-Q1; amplitude dos 50% centrais |
| Z-score | "quantos desvios" | (x-média)/desvio; assume normalidade |
| Outlier | "ponto estranho" | Observação além de Q3+1.5*IQR ou |z|>3 |

## خواندن بیشتر

- [Seeing Theory — Descriptive Stats](https://seeing-theory.brown.edu/) interativo بصری
- [NIST Engineering Statistics Handbook](https://www.itl.nist.gov/div898/handbook/) مرجع
- [SciPy stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) برای تولید
