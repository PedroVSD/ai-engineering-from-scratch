# Distribuições e o Teorema Central do Limite

> 30'luk bir ortalama "sadece normal" veri neden tüm modellerin güven aralığını açıklıyor?

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva, 06-probabilidade-fundamentos
**Time:** ~60 minutes

## Öğrenme Hedefleri

- Uygulama PMF/PDF de Bernoulli, Binomial, Poisson, Normal e Exponencial using só `math`
- Her bir dağıtımın göstergesi`random`e validar média/variância teóricas
- Simular o Teorema Central do Limite: bir mediamostral bir normal için bir araya gelir
- Zıfır komisyon uygulamasını karşılaştır`numpy`- Ne ?`statistics`kullanılabilir olduğunda

## Sorun

Bir API'nin yanıt temposu: media 200ms, mas pios de 5s. É "normal" mı?

## Anlaşım

### Diskretler: Bernoulli → Binomial → Poisson

- **Bernoulli(p):**1 sucesso com prob. p. E[X]=p, Var=p(1-p).
- **Binomial(n,p):**Soma de n Bernoullis. `P(X=k) = C(n,k)·p^k·(1-p)^(n-k)`, E=np, Var=np ((1-p).
- **Poisson(λ):**Raro olaylar var.`P(X=k) = λ^k·e^-λ/k!`, E=Var=λ. Binomial'in sınırlaması n grande, p pequeno, np=λ.

### Sürekli: Normal ve Eksponansiyel

- **Normal(μ,σ):** `f(x) = e^(-(x-μ)²/2σ²)/(σ√2π)`- Simetrica; kural 68-95-99.7.
- **Exponencial(λ):**Poisson'un olayları arasındaki tempo.`f(x) = λ·e^(-λx)`(x≥0), E=1/λ, Var=1/λ2. Sem memória: P(T>s+t t t t t>s)=P(T>t).

### Teorema Central do Limite (TCL)

Eğer x1..xn são i.i.d. com media μ e variância σ2 finita, o zaman:

```
X̄ ~ Normal(μ, σ²/n)  quando n cresce
```

Normal testlerde kullanılan değerler (eşit, eksponensel, ikili)  % 30'dan fazla değil.

```mermaid
flowchart LR
    A[Base qualquer: exp/unif/binom] --> B[Amostra n=30]
    B --> C[Média X-barra]
    C --> D[Repetir 2000x]
    D --> E[Histograma ~ Normal]
    E --> F[IC: X-barra ± 1.96·σ/√n]
```

```figure
stats-distribuicoes-tcl
```

## Yapın

### Adım 1: PMF/PDF sıfır (só `math`)

```python
import math

def bernoulli_pmf(k, p):
    return p if k == 1 else (1 - p if k == 0 else 0.0)

def binom_pmf(k, n, p):
    if not 0 <= k <= n:
        return 0.0
    return math.comb(n, k) * p**k * (1-p)**(n-k)

def poisson_pmf(k, lam):
    return lam**k * math.exp(-lam) / math.factorial(k)

def normal_pdf(x, mu=0.0, sigma=1.0):
    return math.exp(-((x-mu)**2)/(2*sigma**2)) / (sigma * math.sqrt(2*math.pi))

def expon_pdf(x, lam):
    return lam * math.exp(-lam*x) if x >= 0 else 0.0

print(binom_pmf(2, 10, 0.5))   # ~0.0439 (= 45/1024)
print(poisson_pmf(3, 2.0))     # ~0.180
print(normal_pdf(0))           # ~0.399
```

### Adım 2: Amostragem com`random`

```python
import random

def sample_bernoulli(p, rng):
    return 1 if rng.random() < p else 0

def sample_binomial(n, p, rng):
    return sum(sample_bernoulli(p, rng) for _ in range(n))

def sample_poisson(lam, rng):
    # Knuth: conta eventos até exceder e^-λ
    L = math.exp(-lam)
    k, prod = 0, 1.0
    while True:
        k += 1
        prod *= rng.random()
        if prod <= L:
            return k - 1

def sample_expon(lam, rng):
    return -math.log(1 - rng.random()) / lam  # inversa da CDF

def sample_normal(mu, sigma, rng):
    return rng.gauss(mu, sigma)  # Box-Muller interno do CPython

rng = random.Random(0)
print([sample_binomial(10, 0.5, rng) for _ in range(5)])
```

### Adım 3: TCL simülasyonu

```python
def sample_means(sampler, n, reps, rng):
    return [sum(sampler() for _ in range(n)) / n for _ in range(reps)]

rng = random.Random(42)
means = sample_means(lambda: rng.expovariate(1.0), n=30, reps=2000, rng=rng)
m = sum(means) / len(means)
v = sum((x-m)**2 for x in means) / len(means)
print(f"base exp(1): E[X̄]={m:.3f} (→1.0) Var={v:.4f} (→1/30≈0.0333)")
```

## Kullan

Konferencia com`numpy`- Ne ?`statistics`(İsteğe bağlı):

```python
try:
    import numpy as np
    rng = np.random.default_rng(0)
    s = rng.binomial(10, 0.5, size=50_000)
    print(f"[numpy] binomial(10,.5): média={s.mean():.3f} (→5.0) var={s.var():.3f} (→2.5)")
    e = rng.exponential(1.0, size=(2000, 30)).mean(axis=1)
    print(f"[numpy] TCL exp: E[X̄]={e.mean():.3f} Var={e.var():.4f}")
except ImportError:
    print("numpy não instalado — comparação pulada (pip install numpy)")
```

- Evet .`math.comb`Ürünler ve işlevler, PMF'ler için 3a evde anlaşmalı.

## Gönder

Artefato:`outputs/skill-distribuicoes.md` "TCL normal aralığı onayladığında hangi dağıtım kullanılır".

## Egzersizler

1. Binomial n=100, p=0.02) ≈ Poisson λ=2): PMF k=0.5 olarak karşılaştırın.
2. TCL'nin temel üniforması simülasyonunu yeniden yapın.`random.random()`: E[X̄]→0.5 e Var→1/(12·30)?
3. Quebra do TCL: kullanma tabanı Cauchy (`tan(pi*(u-0.5))`O'nun "normalize" gazetesi tarihsel programı, "por quê" (Dic: variância infinita)

## Anahtar Terimler

| Term | O que dizem | O que realmente é |
|---|---|---|
| Bernoulli | "cara ou coroa" | Bloco atômico 0/1 com prob. p |
| Binomial | "k sucessos em n" | Soma de Bernoullis; C(n,k)p^k(1-p)^(n-k) |
| Poisson | "eventos raros" | Limite da Binomial; E=Var=λ |
| Normal | "curva sino" | PDF gaussiana; 68-95-99.7 em ±1/2/3σ |
| Exponencial | "tempo de espera" | Intervalo entre Poissons; sem memória |
| TCL | "média vira normal" | X̄→Normal(μ,σ²/n); exige variância finita |

## Daha Fazla Okumak

- [Seeing Theory — Distributions & CLT](https://seeing-theory.brown.edu/) visual interativo
- [SciPy stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) para üretim
- [NIST: Probability Distributions](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm)Referans
