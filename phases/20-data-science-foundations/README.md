# Phase 20: Data Science Foundations — Piloto

> Do CSV sujo ao primeiro modelo e ao primeiro neurônio — tudo do zero, depois com libs.

**5 aulas piloto** (isoladas do build principal; adicione ao `README.md` raiz quando quiser publicar).

| # | Lesson | Type | Lang | Status |
|---|---|---|---|---|
| 01 | [Estatística Descritiva do Zero](01-estatistica-descritiva/) | Build | Python | ✅ |
| 02 | [Limpeza e EDA do Zero](02-limpeza-e-eda/) | Build | Python | ✅ |
| 03 | [Regressão Linear do Zero](03-regressao-do-zero/) | Build | Python | ✅ |
| 04 | [Classificação e Avaliação](04-classificacao-e-avaliacao/) | Build | Python | ✅ |
| 05 | [Perceptron e Deep Learning do Zero](05-intro-deep-learning-perceptron/) | Build | Python | ✅ |

## Como usar (local)

```bash
python phases/20-data-science-foundations/01-estatistica-descritiva/code/main.py
python -m unittest discover phases/20-data-science-foundations/01-estatistica-descritiva/code/tests -v
# repetir para 02,03,04,05
```

Para publicar no site: adicione as 5 linhas acima na tabela de fases do `README.md` raiz e rode `node site/build.js`.
