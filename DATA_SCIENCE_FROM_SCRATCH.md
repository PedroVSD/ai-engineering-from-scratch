# Data Science from Scratch — Currículo EXPANDIDO (Fusão Completa)

> **Base:** `DATA_SCIENCE_FROM_SCRATCH.md` (20 fases, 523 aulas, piloto 5 aulas) + **Prompt Mestre Ciência de Dados (36 partes, 164 caps)** + **Prompt ML Engineering (53 caps)** + **Prompt MLOps (44 caps)**
> **Resultado:** 20 fases mantidas, expandidas para **~640 aulas / ~420h**. Tudo que estava nos seus 3 arquivos e faltava no meu plano foi incorporado e marcado como **[NOVO]**. Nada foi removido.

**Como usar:** Este arquivo substitui o `DATA_SCIENCE_FROM_SCRATCH.md` anterior. Para publicar no site (`site/build.js`): copie as tabelas de cada fase para `README.md` raiz. O piloto em `phases/20-data-science-foundations/` continua válido e será redistribuído nas fases 02/06/12.

---

## Visão Geral — 20 Fases Expandidas

| Fase | Nome Expandido | Aulas | Horas | Origem |
|---|---|---|---|---|
| 00 | Setup, Reprodutibilidade & Software Engineering para DS | 18 | 20h | Meu 00 + Prompt V cap24 + MLE Parte II + MLOps Parte III-IV |
| 01 | Python, NumPy, Pandas, SciPy | 22 | 22h | Meu 01 + Prompt V cap20-23 |
| 02 | Matemática para DS — Álgebra Linear, Cálculo, Otimização | 24 | 22h | Meu 06 + Prompt II cap5-8 |
| 03 | Probabilidade | 18 | 16h | Prompt III cap9-12 |
| 04 | Estatística | 20 | 18h | Prompt IV cap13-19 + Meu 02 |
| 05 | Aquisição, SQL & Modelagem de Dados | 22 | 20h | Meu 05 + Prompt VI cap25-27 |
| 06 | Data Quality & Data Wrangling | 20 | 18h | Prompt VII cap28-31 + Meu 04 |
| 07 | EDA, Visualização & Storytelling | 18 | 16h | Meu 03 + Prompt VIII cap32-34 |
| 08 | Fundamentos de ML, Pipeline & Baselines | 16 | 14h | Prompt IX cap35-37 + MLE Parte I |
| 09 | Regressão & Regularização | 16 | 16h | Prompt X + Meu 07 |
| 10 | Classificação | 18 | 18h | Prompt XI + Meu 07 |
| 11 | Avaliação, Validação & Tuning | 20 | 18h | Prompt XII-XIII + Meu 08 + MLE cap18 |
| 12 | Feature Engineering & Seleção | 16 | 16h | Prompt XIV + MLE cap13 |
| 13 | Não-Supervisionado, Redução & Anomalias | 18 | 16h | Prompt XV-XVI + Meu 09 |
| 14 | Séries Temporais & Forecasting | 16 | 16h | Prompt XVII + Meu 10 |
| 15 | Recomendação & NLP | 20 | 20h | Prompt XVIII-XIX |
| 16 | Deep Learning Core | 18 | 18h | Prompt XX + Meu 12-13 + Piloto 05 |
| 17 | Arquiteturas DL — CNN, RNN, Transformers, Generativo | 18 | 18h | Prompt XX cap90-92 + Meu 14-16 |
| 18 | Experimentação, Causalidade, Explicabilidade | 16 | 16h | Prompt XXI-XXIII + Meu 11 |
| 19 | MLOps, ML Engineering, Produção & Capstones | 28 | 50h | Prompt XXIV-XXX + MLE cap24-52 + MLOps cap36-44 + Meu 17-19 |
| **Total** | | **~642** | **~420h** | |

---

## Detalhamento Expandido — O que foi adicionado [NOVO]

### FASE 00 — Setup, Reprodutibilidade & Software Engineering para DS (18 aulas)

**Meu original:** 12 aulas (venv, Git, Docker, Jupyter)

**[NOVO] Adicionado de Prompt V cap24 + MLE Parte II + MLOps Parte III-IV:**

| # | Aula | Type | Tópicos [NOVO] |
|---|---|---|---|
| 01 | Dev Environment DS | Build | Python 3.11, uv, pyproject.toml, reproducibilidade |
| 02 | Git & Colaboração | Learn | Branch, PR, pre-commit, Code Review (MLE cap144) |
| 03 | Jupyter & Organização de Projetos | Build | Notebook vs pacote, estrutura `src/`, pyproject (Prompt V cap24) |
| 04 | Ambientes & Dependências | Build | venv, uv, pip-tools, lockfile |
| 05 | Docker para DS | Build | Image, volume, multi-stage (MLE cap24) |
| 06 | Clean Code para DS | Learn | Funções, SOLID, Design Patterns (MLE cap5, Prompt XXVI cap133-136) [NOVO] |
| 07 | Testes — Pirâmide DS | Build | Unit, integração, dados, modelo, pipeline (MLE cap6, Prompt XXVI cap140) [NOVO] |
| 08 | Logging, Exceptions & Config | Build | logging estruturado, YAML/TOML, secrets (MLE cap7-8) [NOVO] |
| 09 | Debugging & Profiling | Build | cProfile, pdb, tracing [NOVO — expandido] |
| 10 | Reprodutibilidade | Learn | seeds, dataset/code/env version, DVC (MLOps cap9) [NOVO] |
| 11 | Experiment Tracking | Build | MLflow, W&B, runs/artifacts (MLE cap15, MLOps cap10) [NOVO] |
| 12 | Data Versioning | Build | DVC, lakehouse versioning (MLOps cap11) [NOVO] |
| 13 | Terminal & Shell | Learn | awk, jq, xsv |
| 14 | Linux para DS | Learn | cron, systemd |
| 15 | Data Management | Build | Parquet, HDF5, zstd |
| 16 | APIs & Keys | Build | .env, rate limit |
| 17 | Polars vs Pandas | Build | Lazy, benchmark |
| 18 | DuckDB Local | Build | Query Parquet sem servidor |

### FASE 01 — Python, NumPy, Pandas, SciPy (22 aulas)

**Meu original:** 6 bullets genéricos

**[NOVO] Expandido de Prompt V cap20-23:**

- Python profundo: iteradores, generators, decorators, context managers, typing (cap20) [NOVO]
- NumPy: ndarray, broadcasting, vectorization, random, linalg (cap21) [NOVO]
- Pandas completo: Series/DataFrame, indexing, groupby, merge/join, pivot/melt, apply/transform, rolling, missing, categorical, datetime (cap22) [NOVO]
- SciPy: estatística, otimização, integração (cap23) [NOVO]
- Projeto: ETL CSV → Pandas/Polars → Parquet

### FASE 02 — Matemática para DS (24 aulas)

**Meu original:** Fase 06 com 4 bullets

**[NOVO] Prompt II cap5-8 completo:**

| # | Aula | Tópicos [NOVO] |
|---|---|---|
| 01 | Conjuntos, Funções, Notação | conjuntos, domínio, imagem, somatórios [NOVO] |
| 02 | Álgebra Linear I | escalares, vetores, matrizes, tensores, transposta, inversa, rank [NOVO] |
| 03 | Álgebra Linear II | espaço vetorial, base, combinação linear, norma, distância, projeções |
| 04 | Decomposições | autovalores/vetores, espectral, SVD, PCA (com geometria) |
| 05 | Cálculo I | limites, derivadas, parciais, gradiente [NOVO] |
| 06 | Cálculo II | Jacobiana, Hessiana, regra da cadeia, convexidade [NOVO] |
| 07 | Otimização I | função objetivo, GD, SGD, mini-batch, learning rate [NOVO] |
| 08 | Otimização II | momentum, Adam, RMSProp, Newton, mínimos locais/globais [NOVO] |

### FASE 03 — Probabilidade (18 aulas) [NOVO — quase todo ausente]

**De Prompt III cap9-12:**

- Fundamentos: espaço amostral, união/interseção, condicional, independência, Bayes
- Variáveis aleatórias: PMF/PDF/CDF, esperança, variância, covariância
- 14 Distribuições: Bernoulli, Binomial, Geométrica, Poisson, Uniforme, Normal, Exponencial, Gamma, Beta, Log-normal, t-Student, Chi-square, F, Normal Multivariada (cada com teoria + aplicação)
- Teoremas: Lei Grandes Números, TCL, Probabilidade Total

### FASE 04 — Estatística (20 aulas)

**Meu original:** 1 aula piloto (média/IQR)

**[NOVO] Prompt IV cap13-19:**

| # | Aula | Tópicos [NOVO] |
|---|---|---|
| 01 | Descritiva | média/mediana/moda, IQR, assimetria, curtose, robustas — **PILOTO 01** |
| 02 | Amostragem | aleatória, estratificada, sistemática, cluster, viés [NOVO] |
| 03 | Estimação | viés, consistência, eficiência, MLE, momentos [NOVO] |
| 04 | Intervalos Confiança | média, proporção, variância, diferença [NOVO] |
| 05 | Testes Hipóteses | H0/H1, p-value, tipo I/II, poder, t, z, qui², ANOVA, não-paramétricos [NOVO] |
| 06 | Correlação | Pearson, Spearman, Kendall, parcial, espúrias [NOVO] |
| 07 | Regressão Estatística | pressupostos, resíduos, heterocedasticidade, multicolinearidade, autocorrelação [NOVO] |

### FASE 05 — Aquisição, SQL & Modelagem (22 aulas)

**Meu original:** 6 bullets

**[NOVO] Prompt VI cap25-27:**

- Fontes: CSV, JSON, XML, APIs, bancos, NoSQL, logs, sensores, streaming, scraping (cap25) [NOVO]
- SQL profundo: SELECT, WHERE, HAVING, JOIN, subqueries, CTE, window (ROW_NUMBER, RANK, LAG/LEAD), CASE, índices, views (cap26) [NOVO]
- Modelagem: relacional, normalização, OLTP/OLAP, warehouse, lake, lakehouse (cap27) [NOVO]

### FASE 06 — Data Quality & Wrangling (20 aulas)

**Meu original:** 1 aula piloto

**[NOVO] Prompt VII cap28-31:**

- Data Quality 6 dimensões: completude, consistência, unicidade, validade, acurácia, integridade (cap28) [NOVO]
- Missing: MCAR/MAR/MNAR, imputação múltipla, KNN (cap29) [NOVO — expandido]
- Outliers: Isolation Forest, LOF, quando remover/preservar (cap30) [NOVO]
- Transformações: scaling, log, Box-Cox, Yeo-Johnson, encoding, binning (cap31) [NOVO]

### FASE 07 — EDA, Visualização & Storytelling (18 aulas)

**Meu original:** 5 bullets

**[NOVO] Prompt VIII cap32-34 + MLE storytelling:**

- EDA: univariada/bivariada/multivariada, numérica/categórica (cap32) [NOVO]
- Visualização: princípios, percepção, dashboards (cap33) [NOVO]
- Storytelling: narrativa, métricas para executivos, erros de visualização (cap34) [NOVO]

### FASE 08 — Fundamentos ML, Pipeline & Baselines (16 aulas)

**Meu original:** não existia como fase

**[NOVO] Prompt IX cap35-37 + MLE Parte I:**

- Tipos: supervisionado, não-supervisionado, semi, self-supervised, bias/variance, over/underfitting [NOVO]
- Pipeline: preprocessing, feature eng, validação, data leakage profundo [NOVO]
- Baselines: estatístico, heurístico, ML [NOVO]
- ML Systems: model vs pipeline vs platform vs system (MLE cap3) [NOVO]

### FASE 09 — Regressão & Regularização (16 aulas)

**Meu original:** Piloto 03

- Linear (mínimos quadrados, matricial), Ridge, Lasso, Elastic Net (geometria), Polynomial, Splines [NOVO — expandido]

### FASE 10 — Classificação (18 aulas)

**Meu original:** Piloto 04

- Logistic, KNN, Naive Bayes, Decision Trees, Random Forest, Boosting, XGBoost, LightGBM, CatBoost (cada com quando usar, hiperparâmetros) [NOVO — expandido]

### FASE 11 — Avaliação, Validação & Tuning (20 aulas)

**Meu original:** 6 bullets

**[NOVO] Prompt XII-XIII + MLE cap18:**

- Classificação: confusion, accuracy, precision, recall, specificity, F1, balanced acc, ROC/PR-AUC, log loss, calibration [NOVO]
- Regressão: MAE, MSE, RMSE, R², adjusted R², MAPE, SMAPE [NOVO]
- Escolha de métrica por custo de erro [NOVO]
- Validação: holdout, K-Fold, Stratified, Group, TimeSeriesSplit, Nested CV [NOVO]
- Tuning: Grid, Random, Bayesian Optimization [NOVO]

### FASE 12 — Feature Engineering & Seleção (16 aulas)

**Meu original:** 6 bullets

**[NOVO] Prompt XIV + MLE cap13-14:**

- Seleção: filtro, wrapper, RFE, mutual info, regularização [NOVO]
- Engineering: encoding, interações, polinomiais, temporais, agregadas, target encoding [NOVO]
- Feature Store: offline/online, registry, point-in-time, skew (MLE cap14) [NOVO]

### FASE 13 — Não-Supervisionado, Redução & Anomalias (18 aulas)

**Meu original:** 4 bullets

**[NOVO] Prompt XV-XVI:**

- Clustering: K-Means, Hierarchical, DBSCAN, HDBSCAN, GMM, Spectral + avaliação Silhouette, Davies-Bouldin, Calinski-Harabasz [NOVO]
- Redução: PCA, Kernel PCA, t-SNE, UMAP (diferenças/limitações) [NOVO]
- Anomalias: estatístico, IQR, Z-score, Isolation Forest, One-Class SVM, LOF, autoencoders [NOVO]

### FASE 14 — Séries Temporais (16 aulas)

**Meu original:** 5 bullets

**[NOVO] Prompt XVII:**

- Fundamentos: timestamp, decomposição, ACF/PACF, estacionariedade, ADF, differencing [NOVO]
- Modelos: Naive, MA, Exp Smoothing, AR/MA/ARMA/ARIMA/SARIMA, Prophet, ML/DL [NOVO]
- Forecasting: backtesting, rolling/expanding window, multi-step, intervalos [NOVO]

### FASE 15 — Recomendação & NLP (20 aulas) [NOVO — faltava fase dedicada]

**De Prompt XVIII-XIX (ausente no meu):**

- Recomendação: collaborative, content-based, KNN, matrix factorization/SVD, implicit, hybrid + avaliação RMSE, Precision@K, MAP, NDCG + projeto completo [NOVO]
- NLP: tokenização, stopwords, stemming, n-grams, TF-IDF, embeddings, Word2Vec, GloVe, Transformers, BERT + aplicações classificação/similarity [NOVO]

### FASE 16 — Deep Learning Core (18 aulas)

**Meu original:** Piloto 05

- Perceptron, MLP, forward, loss, backprop (já piloto) + CNN, RNN, LSTM, GRU, Transformers (Prompt XX cap89-92) [NOVO — expandido]
- Treinamento: batch/epoch, optimizers, dropout, batchnorm, early stopping

### FASE 17 — Arquiteturas DL (18 aulas)

**Meu original:** 3 bullets

**[NOVO] Prompt XX + MLE LLM:**

- CNN profunda, RNN/LSTM/GRU do zero, Transformers, Transfer Learning (fine-tuning) [NOVO]
- Generativo: AE, VAE, GAN, diffusion tabular [NOVO]

### FASE 18 — Experimentação, Causalidade, Explicabilidade (16 aulas)

**Meu original:** 4 bullets A/B

**[NOVO] Prompt XXI-XXIII:**

- A/B: hipótese, randomização, poder, tamanho amostra, Bayesian vs frequentista [NOVO]
- Causalidade: correlação vs causalidade, confounding, DAGs, Potential Outcomes, RCT, Propensity, Matching, IV, DiD [NOVO]
- Explicabilidade: feature importance, permutation, PDP, ICE, SHAP, LIME (limitações) [NOVO]

### FASE 19 — MLOps, ML Engineering, Produção & Capstones (28 aulas)

**Meu original:** 5 bullets

**[NOVO] Fusão MLE (caps 4-52) + MLOps (caps 4-44):**

| Bloco | Tópicos [NOVO] |
|---|---|
| **Engenharia** | Arquitetura projetos ML, Clean Code SOLID, Testes (unit/dados/modelo/pipeline/API), Config YAML/TOML, Logging |
| **Dados em Produção** | Data pipelines (batch/streaming, ETL/ELT, Airflow/Dagster), Data contracts, Feature Store, Training-serving skew |
| **Treinamento** | Reprodutibilidade, Experiment tracking, Training pipelines DAGs, Model Registry (staging/prod, lineage) |
| **Serving** | Inferência (online/batch/async/streaming), FastAPI, BentoML, escalabilidade (horizontal, batching, caching), GPU infra |
| **MLOps** | CI/CD/CT, Docker, Kubernetes (pods, deployments, autoscaling), Monitoring (drift, concept, prediction), Observabilidade (logs/metrics/traces), Alerting |
| **Governança** | Model lineage, Model cards, Responsible AI, LGPD, privacidade [NOVO] |
| **Custos** | Compute, storage, GPU, inference cost [NOVO] |
| **LLMOps** | Tokens, RAG (chunking, vector DB, reranking), prompt versioning, evaluation, agents (MLE cap46-49) [NOVO] |
| **Confiabilidade** | Reliability, deployment (canary, blue-green, shadow, rollback), segurança, idempotência [NOVO] |
| **Projetos** | 10 projetos progressivos do Prompt Mestre capXXIX + 7 projetos MLE + 12 projetos MLOps + Capstone final end-to-end (dados → API → Docker → monitoramento) |

**Ética & Big Data [NOVO]:** Bias, Fairness, LGPD, Responsible AI (Prompt XXVIII), Big Data (Spark/PySpark, batch vs streaming, lakehouse) — incorporados nesta fase.

**Transversais [NOVO]:** Debugging sistemático (Prompt XXXIII — 9 leakages com código errado/correto), Guia de decisão (Prompt XXXIV — árvores "qual algoritmo/métrica usar?"), Glossário (Prompt XXXV), Referências, Exercícios 5 níveis, Implementações do zero (16 algoritmos — Prompt XXXII).

---

## Site — Estrutura Mantida e Expandida

```
site-ds/
  index.html          # landing 20 fases (já existe)
  data.js             # gerado por site/build.js após copiar tabelas deste arquivo para README.md
  phases/20-data-science-foundations/  # piloto redistribuído: 01→Fase04, 03→Fase09, 04→Fase10, 05→Fase16

phases/
  00-setup-.../       # 18 aulas
  01-python-.../      # 22 aulas
  ...
  19-mlops-capstone/  # 28 aulas
```

Nenhuma mudança no parser `site/build.js:1` ou `scripts/audit_lessons.py:1` — só o conteúdo das pastas.

---

## Checklist de Fusão — Tudo que faltava foi adicionado?

- [x] 36 partes do Prompt Mestre → mapeadas nas 20 fases acima
- [x] 53 caps ML Engineering → fases 00, 08, 12, 19
- [x] 44 caps MLOps → fase 19
- [x] 11 projetos + capstone final → fase 19
- [x] Debugging, Guia decisão, Glossário, Referências → fase 19 transversais
- [x] Piloto 5 aulas preservado e redistribuído

**Arquivos originais preservados em `ciencia_dados/` para auditoria. Este arquivo é o novo canônico.**
