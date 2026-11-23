# Distribuições e o Teorema Central do Limite

> ¿Por qué un medio de 30 datos "quasi normales" explica el intervalo de confianza de todo modelo?

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva, 06-probabilidade-fundamentos
**Time:** ~60 minutes

## Objetivos de aprendizaje

- Implementar PMF/PDF de Bernoulli, Binomial, Poisson, Normal y Exponencial usando sólo `math`
- Amostrar de cada distribución com`random`El proyecto de ley de la Unión Europea (UE) no se ha aprobado.
- Simular o Teorema Central do Limite: un medio amostral converge para una normalidad
- Comparar una implementación de la com`numpy`- ¿ Qué ?`statistics`Cuando disponible

## El problema

¿Cómo se puede utilizar el tiempo de respuesta de una API: media 200ms, pero picos de 5s? É "normal"? ¿Puedo usar el medio ± 2·desvio como intervalo? Se una distribución de base exponencial (asimetrica), una respuesta individual no es normal  mas un medio de 30 requisiciones é.

## El concepto

### Discretas: Bernoulli → Binomio → Poisson

- **Bernoulli(p):**1 sucesso com prob. p. E[X]=p, Var=p(1-p).
- **Binomial(n,p):**El Consejo Europeo ha adoptado una decisión sobre el tema.`P(X=k) = C(n,k)·p^k·(1-p)^(n-k)`, E=np, Var=np ((1-p).
- **Poisson(λ):**eventos raros por intervalo. `P(X=k) = λ^k·e^-λ/k!`, E=Var=λ. Limite de la binomial cuando n grande, p pequeño, np=λ.

### Continuas: Normal y exponencial

- **Normal(μ,σ):** `f(x) = e^(-(x-μ)²/2σ²)/(σ√2π)`- Simétrica; reglas 68-95-99.7.
- **Exponencial(λ):**El tiempo entre eventos de Poisson. `f(x) = λ·e^(-λx)`(x≥0), E=1/λ, Var=1/λ2. Sem memória: P(T>s+t t t t>s)=P(T>t).

### Teorema Central do Limite (TCL)

Si X1..Xn son i.i.d. com media μ e variancia σ2 finita, entonces:

```
X̄ ~ Normal(μ, σ²/n)  quando n cresce
```

Vale para cualquier base (uniforme, exponencial, binomial)  por ello medias de n≥30 se tratan como normales en testes A/B.

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

## Construye el mismo

### Paso 1: PMF/PDF hacer cero (só `math`(en inglés)

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

### Paso 2: Amostragem com`random`

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

### Paso 3: Simulación o TCL

```python
def sample_means(sampler, n, reps, rng):
    return [sum(sampler() for _ in range(n)) / n for _ in range(reps)]

rng = random.Random(42)
means = sample_means(lambda: rng.expovariate(1.0), n=30, reps=2000, rng=rng)
m = sum(means) / len(means)
v = sum((x-m)**2 for x in means) / len(means)
print(f"base exp(1): E[X̄]={m:.3f} (→1.0) Var={v:.4f} (→1/30≈0.0333)")
```

## Usalo

Conferencia com`numpy`- ¿ Qué ?`statistics`(opcional):

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

Su `math.comb`El Consejo de Ministros de Finanzas de la Unión Europea (UE) aprobó el artículo 3 del Tratado de Maastricht.

## Envío

Artefato: `outputs/skill-distribuicoes.md` guía "cuál es la distribución de uso + cuando el TCL autoriza el intervalo normal".

## Los ejercicios

1. Muestre numericamente que Binomial ((n=100, p=0.02) ≈ Poisson ((λ=2): compare como PMF k=0.5.
2. Refaça una simulación del uniforme de base TCL `random.random()`¿Qué es esto?
3. Quebra do TCL: base de uso Cauchy (`tan(pi*(u-0.5))`¿O histograma das médias "normaliza"? Por qué?

## Términos clave

| Term | O que dizem | O que realmente é |
|---|---|---|
| Bernoulli | "cara ou coroa" | Bloco atômico 0/1 com prob. p |
| Binomial | "k sucessos em n" | Soma de Bernoullis; C(n,k)p^k(1-p)^(n-k) |
| Poisson | "eventos raros" | Limite da Binomial; E=Var=λ |
| Normal | "curva sino" | PDF gaussiana; 68-95-99.7 em ±1/2/3σ |
| Exponencial | "tempo de espera" | Intervalo entre Poissons; sem memória |
| TCL | "média vira normal" | X̄→Normal(μ,σ²/n); exige variância finita |

## Leer más

- [Seeing Theory — Distributions & CLT](https://seeing-theory.brown.edu/) Interativo visual
- [SciPy stats docs](https://docs.scipy.org/doc/scipy/reference/stats.html) para la producción
- [NIST: Probability Distributions](https://www.itl.nist.gov/div898/handbook/eda/section3/eda366.htm) referencia
