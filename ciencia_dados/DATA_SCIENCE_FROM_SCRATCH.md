# Data Science from Scratch — Currículo Completo

> 523 aulas • 20 fases • ~350 horas • Python, SQL, Rust opcional • Do CSV sujo ao modelo em produção. Primeiro a matemática pura, depois a biblioteca. Todo `site` roda 100% local.

Este arquivo é o **mapa canônico** para reconstruir o projeto `ai-engineering-from-scratch` voltado para Ciência de Dados + Deep Learning. Use-o como `ROADMAP.md` alternativo. A estrutura de pastas, contrato de aula e `site/build.js` continuam idênticos — só o conteúdo muda.

---

## Como o site funciona (já pronto)

```
phases/20-data-science-foundations/  # piloto já criado (5 aulas)
phases/01-fundamentos/ ...            # novas fases (a criar)
site-ds/                             # site piloto local (já roda: python -m http.server 8000 --directory site-ds)
site/build.js                        # parser oficial — lê README.md + ROADMAP.md -> site/data.js
```

Para publicar no site oficial: copie as tabelas de fases deste arquivo para o `README.md` raiz e rode `node site/build.js`. O piloto atual está isolado em `phases/20-*` justamente para não quebrar o build até você aprovar.

---

## Filosofia (mesma do projeto original)

1. **Build It / Use It**: implementa do zero com `stdlib` + `numpy`, depois repete com `pandas`/`sklearn`/`torch`.
2. **Stdlib-first**: `numpy`, `torch`, `pandas`, `polars`, `duckdb`, `scikit-learn`, `matplotlib` — sem dependências exóticas.
3. **Cada aula entrega artefato**: `outputs/skill-*.md`, `prompt-*.md` ou `agent-*.md` reutilizável.
4. **Site local**: `site-ds/index.html` já funciona offline; `site/` oficial gera `data.js` via CI.

---

## Visão das 20 Fases

| Fase | Nome | Horas | Foco |
|---|---|---|---|
| 00 | Setup & Tooling DS | 12h | Ambiente, Git, Docker, Jupyter, uv/venv |
| 01 | Python & SQL Fundamentos | 18h | Estruturas, SQL, DuckDB |
| 02 | Estatística Descritiva & Probabilidade | 16h | Centro, dispersão, Bayes |
| 03 | Visualização & EDA | 14h | Matplotlib, Seaborn, Plotly |
| 04 | Limpeza & Qualidade de Dados | 16h | Missing, deduplicação, validação |
| 05 | Modelagem de Dados & SQL Avançado | 18h | Normalização, Window, CTE |
| 06 | Álgebra Linear & Otimização para DS | 14h | Vetores, SVD, PCA, GD |
| 07 | Regressão & Classificação Clássica | 20h | Linear, Logística, Árvores, kNN, SVM |
| 08 | Avaliação, Validação & Feature Engineering | 18h | CV, métricas, encoding, scaling |
| 09 | Não-Supervisionado | 14h | K-Means, DBSCAN, Hierárquico, UMAP |
| 10 | Séries Temporais & Forecasting | 16h | Decomposição, ARIMA, Prophet |
| 11 | Experimentação & A/B Testing | 12h | Teste t, poder, causalidade |
| 12 | Redes Neurais Fundamentos | 16h | Perceptron, Backprop, MLP |
| 13 | Deep Learning Core | 18h | SGD, Adam, Dropout, BatchNorm, Init |
| 14 | CNNs para Dados Tabulares/Imagem | 16h | Convolução, ResNet, Transfer |
| 15 | RNNs, Attention & Transformers | 18h | LSTM, Attention, ViT tabular |
| 16 | Generativo & Autoencoders | 14h | AE, VAE, Embeddings |
| 17 | MLOps & Deploy | 16h | Pipeline, API, Monitoramento |
| 18 | Capstone Tabular | 30h | Projeto end-to-end |
| 19 | Capstone Deep Learning + Portfólio | 35h | Dashboard, Storytelling, Deploy |

**Total: ~341h** (523 aulas, média 39min/aula)

---

## Detalhamento por Fase e Tópicos

### Fase 00 — Setup & Tooling DS (12 aulas)

| # | Aula | Type | Tópicos |
|---|---|---|---|
| 01 | Dev Environment DS | Build | Python 3.11, uv/venv, VS Code, terminal |
| 02 | Git & Colaboração | Learn | Branch, PR, pre-commit |
| 03 | Jupyter & Marimo | Build | Notebook reprodutível, widgets |
| 04 | Docker para DS | Build | Imagem, volume, compose |
| 05 | Gerenciamento de Dados | Build | Parquet, HDF5, zstd, DVC |
| 06 | SQL Básico | Build | SELECT, JOIN, GROUP BY |
| 07 | DuckDB Local | Build | Query em Parquet/CSV sem servidor |
| 08 | Polars vs Pandas | Build | Lazy, streaming, benchmark |
| 09 | Terminal & Shell | Learn | awk, jq, xsv |
| 10 | Linux para DS | Learn | cron, systemd, logs |
| 11 | Debugging & Profiling | Build | cProfile, memory_profiler |
| 12 | APIs & Keys | Build | .env, secrets, rate limit |

*Artefatos: `skill-ambiente-ds`, `prompt-debug-pandas`*

### Fase 01 — Python & SQL Fundamentos (18 aulas)

- Tipos, listas, dicts, comprehensions, generators, decorators
- OOP para pipelines, dataclasses, typing
- Manipulação de strings, regex, datas
- SQL: SELECT, WHERE, JOIN (inner/left/right), UNION
- Subqueries, CTEs simples, agregações
- Projeto: ETL mini com CSV → DuckDB → Parquet

### Fase 02 — Estatística Descritiva & Probabilidade (16 aulas) — ✅ PILOTO 01

| # | Aula | Tópicos |
|---|---|---|
| 01 | Estatística Descritiva do Zero | média, mediana, moda, var, std, quartis, IQR, z-score, histograma — **PILOTO PRONTO** |
| 02 | Distribuições | Normal, Bernoulli, Binomial, Poisson, Exponencial |
| 03 | Teorema de Bayes | Bayes, prior/posterior, naive Bayes manual |
| 04 | Intervalo de Confiança | IC, bootstrap |
| 05 | Testes de Hipótese | p-valor, t-test, chi² |
| 06 | Correlação vs Causalidade | Pearson, Spearman, confounders |

### Fase 03 — Visualização & EDA (14 aulas)

- Gramática dos gráficos (Wilkinson), tipos: linha, barra, scatter, box, violin, heatmap
- Matplotlib do zero (figure, axes), Seaborn, Plotly
- EDA: `describe()`, `info()`, correlograma, pairplot
- Storytelling: quando usar qual gráfico, mentiras com escala
- Projeto: Dashboard EDA com matplotlib + Streamlit

### Fase 04 — Limpeza & Qualidade de Dados (16 aulas) — ✅ PILOTO 02

| # | Aula | Tópicos |
|---|---|---|
| 01 | Limpeza e EDA do Zero | missing (MCAR/MAR/MNAR), imputação, dedup, Pearson — **PILOTO PRONTO** |
| 02 | Tipos & Parsing | datas, moeda, encoding, UTF-8 |
| 03 | Outliers | IQR, z-score, Isolation Forest manual |
| 04 | Validação | Great Expectations, pandera, constraints |
| 05 | Dado Desbalanceado | Oversample, undersample, SMOTE do zero |
| 06 | Texto Sujo | Normalização, n-grams, TF-IDF |

### Fase 05 — Modelagem de Dados & SQL Avançado (18 aulas)

- Normalização 1FN/2FN/3FN, chaves, índices
- Window Functions: ROW_NUMBER, RANK, LAG/LEAD, running sum
- CTEs recursivas, PIVOT, JSON columns
- Modelagem estrela vs. normalizada (fato/dimensão)
- Projeto: Data Warehouse local com DuckDB + dbt

### Fase 06 — Álgebra Linear & Otimização (14 aulas)

- Vetores, matrizes, normas, distâncias (euclidiana, cosseno, Manhattan)
- Decomposição: SVD, eigendecomposição, PCA do zero
- t-SNE, UMAP intuição
- Gradiente descendente, convexidade, learning rate

### Fase 07 — Regressão & Classificação Clássica (20 aulas) — ✅ PILOTO 03/04

| # | Aula | Tópicos |
|---|---|---|
| 01 | Regressão Linear do Zero | GD, equação normal, R², Ridge — **PILOTO 03 PRONTO** |
| 02 | Regressão Logística | Sigmoide, BCE, matriz confusão — **PILOTO 04 PRONTO** |
| 03 | kNN & Distâncias | k, ponderação, curse of dimensionality |
| 04 | Árvores de Decisão | Gini, entropia, poda |
| 05 | Random Forest & Bagging | Bootstrap, OOB |
| 06 | Boosting | AdaBoost, XGBoost, LightGBM intuição |
| 07 | SVM | Margem, kernel trick |
| 08 | Naive Bayes | Multinomial, Gaussiano |

### Fase 08 — Avaliação, Validação & Feature Engineering (18 aulas)

- Train/test split, K-Fold, Stratified, TimeSeriesSplit
- Métricas: MSE, RMSE, MAE, R², Precisão, Recall, F1, AUC, PR-AUC
- Curva ROC, Precision-Recall, lift
- Encoding: one-hot, target, frequency, embeddings
- Scaling: standard, min-max, robust, quantile
- Seleção: filtro, wrapper, L1, Boruta
- Projeto: Pipeline `sklearn` reprodutível

### Fase 09 — Não-Supervisionado (14 aulas)

- K-Means, K-Means++ do zero, elbow, silhueta
- DBSCAN, Hierárquico, GMM
- Redução: PCA, UMAP, t-SNE
- Regras de associação (Apriori)

### Fase 10 — Séries Temporais & Forecasting (16 aulas)

- Decomposição tendência/sazonalidade/ruído
- Média móvel, EWMA, AR, MA, ARIMA
- Prophet, NeuralProphet
- Avaliação: MAPE, sMAPE, MASE; backtesting
- Projeto: Forecast de vendas com sazonalidade

### Fase 11 — Experimentação & A/B Testing (12 aulas)

- Teste A/B: poder, tamanho de amostra, peeking
- CUPED, variance reduction
- Causalidade: DAG, confounders, diff-in-diff
- Projeto: Plataforma A/B local com GrowthBook

### Fase 12 — Redes Neurais Fundamentos (16 aulas) — ✅ PILOTO 05

| # | Aula | Tópicos |
|---|---|---|
| 01 | Perceptron & MLP do Zero | Rosenblatt, ReLU, backprop, XOR — **PILOTO 05 PRONTO** |
| 02 | Funções de Ativação | Sigmoid, ReLU, GELU, Swish |
| 03 | Loss Functions | MSE, CE, Focal |
| 04 | Backprop na mão | Cálculo manual com numpy |

### Fase 13 — Deep Learning Core (18 aulas)

- Otimizadores: SGD, Momentum, Adam, AdamW
- Inicialização: Xavier, He; estabilidade
- Regularização: Dropout, Weight Decay, BatchNorm, LayerNorm
- LR schedules, warmup, gradient clipping
- Mini-framework numpy → PyTorch
- Debugging de redes (loss NaN, dead ReLU)

### Fase 14 — CNNs (16 aulas)

- Convolução do zero, padding, stride, pooling
- LeNet a ResNet, transfer learning
- Aplicação tabular: CNN 1D para séries
- Projeto: Classificação com CNN + augment

### Fase 15 — RNNs, Attention & Transformers (18 aulas)

- RNN, LSTM, GRU do zero
- Attention, Multi-Head, Positional Encoding
- Transformer para séries/tabular
- Projeto: Forecasting com Transformer

### Fase 16 — Generativo & Autoencoders (14 aulas)

- Autoencoder, VAE, embeddings
- GAN intuição, diffusion para tabular
- Projeto: Geração de dados sintéticos

### Fase 17 — MLOps & Deploy (16 aulas)

- Pipeline: Polars + DuckDB + sklearn
- API: FastAPI/Hono, batch vs online
- Monitoramento: drift, PSI, Evidently
- Quantização, caching, custo
- Projeto: Modelo em API + dashboard Evidently

### Fase 18 — Capstone Tabular (30h)

- Dataset real (ex: crédito, churn, vendas)
- EDA → limpeza → feature eng → baseline → tuning → validação → relatório
- Entrega: Notebook + API + dashboard Streamlit

### Fase 19 — Capstone Deep Learning + Portfólio (35h)

- Projeto DL (visão tabular ou NLP leve) + deploy
- Storytelling: narrativa, visual, métricas de negócio
- Portfólio: GitHub Pages + `site-ds` + currículo
- Entrega: `outputs/portfolio-*.md` + site publicado

---

## Site — Estrutura Proposta

```
site-ds/
  index.html          # landing com 20 fases (já criado)
  phases/             # espelho de phases/ com links para docs/en.md
  assets/             # logos, diagramas Mermaid/SVG
  data.js             # gerado por site/build.js após publicar
  app.js              # busca, progresso, quiz
  style.css

phases/
  00-setup-tooling/
  01-python-sql-fundamentos/
  ...
  20-data-science-foundations/  # piloto atual (será renomeado para 02/07/12)
```

Comandos:

```bash
# desenvolvimento
python -m http.server 8000 --directory site-ds

# publicar (quando aprovar piloto)
# 1. copiar tabelas deste arquivo para README.md raiz
# 2. node site/build.js
# 3. python scripts/audit_lessons.py
```

---

## Dependências (allowlist estendida para DS)

| Lang | Permitidas |
|---|---|
| Python | `numpy`, `pandas`, `polars`, `duckdb`, `scikit-learn`, `matplotlib`, `seaborn`, `plotly`, `torch`, `h5py`, `zstandard`, `safetensors`, stdlib |
| SQL | DuckDB, SQLite |
| Site | `hono`, `zod`, Node 20+ |

---

## Roadmap de Implementação

| Etapa | Entrega | Status |
|---|---|---|
| 1 | Piloto 5 aulas + site-ds local | ✅ Feito |
| 2 | Fase 00 + 01 completas (30 aulas) | Próximo |
| 3 | Fases 02-08 (core DS, ~120 aulas) | Após 2 |
| 4 | Fases 12-17 Deep Learning (~80 aulas) | Após 3 |
| 5 | Capstones 18-19 + publicação `site/build.js` | Final |

> Cada fase segue `one commit per lesson` (`feat(phase-NN/MM): slug`) e precisa de 5+ testes (`python -m unittest discover`).

---

## Referências Canônicas

- ISLR (James et al.) — regressão, árvores, resampling — https://www.statlearning.com/
- ESL (Hastie et al.) — fundamento matemático — https://hastie.su.domains/ElemStatLearn/
- NIST Handbook — estatística — https://www.itl.nist.gov/div898/handbook/
- CS229 (Andrew Ng) — ML — https://cs229.stanford.edu/main_notes.pdf
- Dive into Deep Learning (Aston Zhang) — DL — https://d2l.ai/

---

*Gerado em 2026-09-17. Piloto em `phases/20-data-science-foundations/`. Site piloto em `site-ds/index.html`.*
