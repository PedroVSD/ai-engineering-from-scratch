# Phase 20: Data Science Foundations — Piloto

> Do CSV sujo ao primeiro modelo e ao primeiro neurônio — tudo do zero, depois com libs.

**9 aulas** (5 piloto + 4 expansão: Fase 03 Probabilidade + Fase 00 Engenharia). Isoladas do build principal.

| # | Lesson | Type | Lang | Status | Origem |
|---|---|---|---|---|---|
| 01 | [Estatística Descritiva do Zero](01-estatistica-descritiva/) | Build | Python | ✅ | Piloto |
| 02 | [Limpeza e EDA do Zero](02-limpeza-e-eda/) | Build | Python | ✅ | Piloto |
| 03 | [Regressão Linear do Zero](03-regressao-do-zero/) | Build | Python | ✅ | Piloto |
| 04 | [Classificação e Avaliação](04-classificacao-e-avaliacao/) | Build | Python | ✅ | Piloto |
| 05 | [Perceptron e Deep Learning do Zero](05-intro-deep-learning-perceptron/) | Build | Python | ✅ | Piloto |
| 06 | [Probabilidade do Zero](06-probabilidade-fundamentos/) | Build | Python | ✅ | Fase 03 [NOVO] |
| 07 | [Distribuições e TCL](07-distribuicoes-tcl/) | Build | Python | ✅ | Fase 03 [NOVO] |
| 08 | [Clean Code e Testes para DS](08-clean-code-testes-ds/) | Build | Python | ✅ | Fase 00 [NOVO] |
| 09 | [Reprodutibilidade e Tracking](09-reprodutibilidade-tracking/) | Build | Python | ✅ | Fase 00 [NOVO] |

## Como usar (local)

```bash
python phases/20-data-science-foundations/01-estatistica-descritiva/code/main.py
python -m unittest discover phases/20-data-science-foundations/01-estatistica-descritiva/code/tests -v
# repetir para 02,03,04,05
```

Para publicar no site: adicione as 5 linhas acima na tabela de fases do `README.md` raiz e rode `node site/build.js`.
