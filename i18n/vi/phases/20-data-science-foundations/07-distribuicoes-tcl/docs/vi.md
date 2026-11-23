# Distribuições e o Teorema Trung tâm do Limite

> Vì sao một trung bình 30 dữ liệu "quasi bình thường" giải thích khoảng thời gian de confiance de tout modèle?

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva, 06-probabilidade-fundamentos
**Time:** ~60 minutes

## Mục tiêu học tập

- Thực thi PMF/PDF de Bernoulli, Binomial, Poisson, Normal e Exponencial sử dụng chỉ `math`
- Amostrar de cada distribuição com `random`e validar media/variância teóricas
- Simular o Theorema Central do Limite: một phương tiện trung bình hội tụ sang một bình thường
- So sánh một thực hiện do zero com `numpy`- Không.`statistics`khi sẵn sàng

## Vấn đề

Bạn đã có một thời gian phản ứng của một API: trung bình 200ms, nhưng có thể đạt 5s. É "normal"? Tôi có thể sử dụng trung bình ± 2·desvio como intervalo? Se una distribución base é exponencial (assimétrica), một đáp ứng cá nhân không phải là bình thường  mas un medio de 30 requisições é.

## Khái niệm

### Các điểm riêng biệt: Bernoulli → Binomial → Poisson

- **Bernoulli(p):**1 sucesso com prob. p. E[X]=p, Var=p(1-p).
- **Binomial(n,p):**- Thì, tôi không biết.`P(X=k) = C(n,k)·p^k·(1-p)^(n-k)`, E=np, Var=np ((1-p).
- **Poisson(λ):**Sự kiện hiếm hoi mỗi khoảng thời gian. `P(X=k) = λ^k·e^-λ/k!`, E=Var=λ. Biên giới của Binomial khi n grande, p pequeno, np=λ.

### Continuas: Normal e Exponencial

- **Normal(μ,σ):** `f(x) = e^(-(x-μ)²/2σ²)/(σ√2π)`- Tương tự; quy định 68-95-99.7.
- **Exponencial(λ):**Tempo entre événements de Poisson. `f(x) = λ·e^(-λx)`(x≥0), E=1/λ, Var=1/λ2.

### Các lý thuyết trung tâm do Limite (TCL)

Nếu x1..xn são i.i.d. com media μ e variância σ2 finita, thì:

```
X̄ ~ Normal(μ, σ²/n)  quando n cresce
```

Vale para qualquer base (uniforme, exponencial, binomial)  por isso medias de n≥30 se tratam como normais em testes A/B.

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

## Hãy xây dựng nó

### Bước 1: PMF/PDF làm không (só `math`(văn)

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

### Bước 2: Amostragem com`random`

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

### Bước 3: TCL

```python
def sample_means(sampler, n, reps, rng):
    return [sum(sampler() for _ in range(n)) / n for _ in range(reps)]

rng = random.Random(42)
means = sample_means(lambda: rng.expovariate(1.0), n=30, reps=2000, rng=rng)
m = sum(means) / len(means)
v = sum((x-m)**2 for x in means) / len(means)
print(f"base exp(1): E[X̄]={m:.3f} (→1.0) Var={v:.4f} (→1/30≈0.0333)")
```

## Sử dụng nó

Hội nghị`numpy`- Không.`statistics`(bọn tùy chọn):

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

Seu `math.comb`Các cơ quan và các cơ quan phải đồng thuận với các cơ quan quản lý.

## Chuyển nó

Artefato: `outputs/skill-distribuicoes.md` hướng dẫn "quan phân phối sử dụng + khi TCL cho phép khoảng thời gian bình thường".

## Các bài tập

1. Tương tự số hóa số hóa số n=100, p=0.02) ≈ Poisson (λ=2): so sánh với PMFs k=0.5.
2. Refaça a simulação do TCL com base uniform `random.random()`: E[X̄]→0.5 e Var→1/(12·30)?
3. Quebra do TCL: sử dụng cơ sở Cauchy (`tan(pi*(u-0.5))`O histograma das médias "tự bình thường hóa"?

## Các điều khoản chính

| Term | O que dizem | O que realmente é |
|---|---|---|
| Bernoulli | "cara ou coroa" | Bloco atômico 0/1 com prob. p |
| Binomial | "k sucessos em n" | Soma de Bernoullis; C(n,k)p^k(1-p)^(n-k) |
| Poisson | "eventos raros" | Limite da Binomial; E=Var=λ |
| Normal | "curva sino" | PDF gaussiana; 68-95-99.7 em ±1/2/3σ |
| Exponencial | "tempo de espera" | Intervalo entre Poissons; sem memória |
| TCL | "média vira normal" | X̄→Normal(μ,σ²/n); exige variância finita |

## Đọc thêm

- [Seeing Theory — Distributions & CLT](https://seeing-theory.brown.edu/) visual interativo
- [SciPy stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) để sản xuất
- [NIST: Probability Distributions](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm) Reference
