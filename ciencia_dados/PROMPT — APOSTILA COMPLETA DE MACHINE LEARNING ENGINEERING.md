# PROMPT — APOSTILA COMPLETA DE MACHINE LEARNING ENGINEERING

Você é um **Staff Machine Learning Engineer, Software Engineer e MLOps Engineer**, com experiência prática na construção, operação e evolução de sistemas de Machine Learning em produção.

Sua tarefa é criar uma **apostila completa, profissional e tecnicamente rigorosa sobre Machine Learning Engineering**, voltada para alguém que deseja desenvolver competência real para atuar como **Machine Learning Engineer**, e não apenas aprender a treinar modelos.

A apostila deve ter caráter de **material de formação profissional**, combinando fundamentos teóricos, engenharia de software, engenharia de dados, Machine Learning, MLOps, sistemas distribuídos, infraestrutura, observabilidade e deployment.

O objetivo final é que o leitor consiga compreender e construir o ciclo completo:

**Problem → Data → Experiment → Train → Evaluate → Package → Deploy → Serve → Monitor → Retrain**

---

# 1. OBJETIVO DA APOSTILA

A apostila deve responder progressivamente:

- O que faz um Machine Learning Engineer?
- Como ML Engineering se diferencia de Data Science, Data Engineering, Software Engineering e MLOps?
- Como transformar um experimento de Machine Learning em um sistema de produção?
- Como projetar pipelines de dados e treinamento?
- Como garantir qualidade e reprodutibilidade?
- Como disponibilizar modelos como serviços?
- Como escalar inferência?
- Como monitorar modelos e dados?
- Como automatizar treinamento e deployment?
- Como projetar sistemas de ML robustos?
- Como lidar com custo, latência, disponibilidade e escalabilidade?
- Como tomar decisões arquiteturais em sistemas de ML?

A apostila não deve tratar ML como apenas "treinar um modelo".

O foco deve ser:

> **Machine Learning como sistema de software operando em produção.**

---

# 2. PERFIL DO LEITOR

Considere um leitor com conhecimento prévio de:

- Python;
- programação;
- estruturas de dados;
- Git;
- fundamentos de Machine Learning;
- SQL básico/intermediário;
- Linux básico.

Porém, não presuma conhecimento profundo de:

- arquitetura de software;
- APIs;
- sistemas distribuídos;
- cloud;
- MLOps;
- containers;
- orquestração;
- observabilidade;
- data engineering.

Explique os conceitos necessários antes de utilizá-los.

Não simplifique excessivamente os conceitos técnicos.

A apostila deve formar raciocínio de engenharia.

---

# 3. PRINCÍPIOS DIDÁTICOS

Cada capítulo deve seguir, sempre que aplicável, esta estrutura:

## Conceito

Explique o conceito de maneira rigorosa.

## Por que isso existe?

Explique qual problema de engenharia ele resolve.

## Como funciona?

Explique internamente o mecanismo.

## Arquitetura

Mostre como o componente se encaixa em um sistema maior.

## Implementação

Apresente exemplos práticos.

## Problemas comuns

Mostre como as coisas podem dar errado.

## Trade-offs

Explique vantagens, desvantagens e quando escolher cada abordagem.

## Produção

Explique como o conceito muda quando sai de um notebook e entra em produção.

## Exercícios

Proponha exercícios progressivos.

## Projeto

Quando fizer sentido, conecte o capítulo a um projeto maior.

---

# 4. ESTRUTURA PRINCIPAL DA APOSTILA

Organize a apostila aproximadamente nas seguintes partes.

---

# PARTE I — FUNDAMENTOS DE MACHINE LEARNING ENGINEERING

## 1. O que é Machine Learning Engineering?

Explique:

- definição;
- responsabilidades;
- competências;
- relação com Data Science;
- relação com Software Engineering;
- relação com Data Engineering;
- relação com MLOps;
- relação com DevOps;
- ML Engineer vs MLOps Engineer;
- ML Engineer vs Data Scientist.

Mostre exemplos reais de responsabilidades.

---

## 2. O ciclo de vida de Machine Learning

Apresente o ciclo:

```text
Problem Definition
       ↓
Data Collection
       ↓
Data Validation
       ↓
Feature Engineering
       ↓
Experimentation
       ↓
Training
       ↓
Evaluation
       ↓
Model Packaging
       ↓
Deployment
       ↓
Inference
       ↓
Monitoring
       ↓
Retraining
```

Explique cada etapa.

Mostre por que o modelo é apenas uma pequena parte do sistema.

---

## 3. Machine Learning Systems

Explique a diferença entre:

- ML model;
- ML pipeline;
- ML application;
- ML platform;
- ML system.

Apresente exemplos arquiteturais.

---

# PARTE II — SOFTWARE ENGINEERING PARA ML

## 4. Arquitetura de projetos de ML

Explique:

- organização de código;
- separation of concerns;
- modularização;
- domínio;
- infraestrutura;
- configuração;
- adapters;
- services;
- repositories.

Apresente uma estrutura profissional de projeto Python.

---

## 5. Clean Code aplicado a ML

Aborde:

- funções;
- classes;
- interfaces;
- abstrações;
- dependency injection;
- typing;
- dataclasses;
- princípios SOLID;
- composição vs herança;
- código testável.

Mostre exemplos ruins e versões melhores.

---

## 6. Testes em sistemas de ML

Explique:

- unit tests;
- integration tests;
- end-to-end tests;
- data tests;
- model tests;
- pipeline tests;
- regression tests;
- contract tests.

Explique também o que significa testar um modelo probabilístico.

---

## 7. Configuração e gerenciamento de experimentos

Explique:

- YAML;
- TOML;
- environment variables;
- configuration objects;
- secrets;
- parâmetros de treinamento;
- configuração por ambiente.

Mostre como evitar hard-code.

---

## 8. Logging, exceptions e debugging

Explique:

- logging estruturado;
- níveis de log;
- tracing;
- exception handling;
- debugging;
- correlation IDs.

Mostre exemplos para pipelines e serviços de inferência.

---

# PARTE III — DATA ENGINEERING PARA MACHINE LEARNING

## 9. Dados como parte do sistema

Explique:

- data sources;
- ingestion;
- storage;
- processing;
- transformation;
- serving.

Mostre arquiteturas:

```text
Source → Ingestion → Storage → Processing → Feature/Data Store
```

---

## 10. Data pipelines

Aborde:

- batch;
- streaming;
- ETL;
- ELT;
- orchestration;
- scheduling;
- dependencies;
- retries;
- idempotência.

---

## 11. Data quality

Explique:

- schema validation;
- nulls;
- duplicates;
- ranges;
- outliers;
- distributions;
- constraints;
- freshness;
- completeness;
- consistency.

Explique data contracts.

---

## 12. Data leakage

Explique profundamente:

- target leakage;
- train/test contamination;
- temporal leakage;
- preprocessing leakage;
- feature leakage.

Inclua exemplos práticos.

---

## 13. Feature Engineering

Aborde:

- numerical features;
- categorical features;
- text;
- temporal features;
- aggregations;
- normalization;
- encoding;
- feature selection.

Explique problemas de treinamento vs inferência.

---

## 14. Feature Store

Explique:

- conceito;
- offline store;
- online store;
- feature serving;
- point-in-time correctness;
- training-serving skew.

Discuta quando utilizar e quando não utilizar.

---

# PARTE IV — EXPERIMENTAÇÃO E TREINAMENTO

## 15. Experiment tracking

Explique:

- parâmetros;
- métricas;
- artifacts;
- datasets;
- modelos;
- experimentos;
- runs.

Mostre como reproduzir um experimento.

---

## 16. Reprodutibilidade

Explique:

- random seeds;
- environment;
- dependencies;
- dataset version;
- code version;
- model version;
- configuration version.

Explique por que "mesmo código" não significa necessariamente "mesmo resultado".

---

## 17. Training pipelines

Projete pipelines completos:

```text
Load Data
   ↓
Validate
   ↓
Transform
   ↓
Train
   ↓
Evaluate
   ↓
Register
```

Explique cada etapa.

---

## 18. Model evaluation

Aborde:

- métricas;
- validation;
- cross-validation;
- holdout;
- temporal split;
- class imbalance;
- calibration;
- threshold selection.

Discuta métricas offline vs métricas de negócio.

---

## 19. Model registry

Explique:

- model versions;
- staging;
- production;
- promotion;
- rollback;
- lineage.

---

# PARTE V — MODEL SERVING

## 20. Inferência

Explique:

- online inference;
- batch inference;
- asynchronous inference;
- streaming inference.

Compare:

```text
Batch
Online
Async
Streaming
```

---

## 21. APIs para Machine Learning

Utilize FastAPI como exemplo.

Explique:

- endpoints;
- schemas;
- validation;
- serialization;
- health checks;
- readiness;
- liveness;
- error handling;
- versioning.

Mostre como servir um modelo corretamente.

---

## 22. Performance de inferência

Explique:

- latency;
- throughput;
- concurrency;
- batching;
- caching;
- CPU;
- GPU;
- memory;
- model loading.

Explique P50, P95 e P99.

---

## 23. Model packaging

Aborde:

- serialization;
- artifacts;
- dependencies;
- environment;
- model formats;
- reproducibility.

Explique problemas de incompatibilidade entre ambientes.

---

# PARTE VI — CONTAINERS E INFRAESTRUTURA

## 24. Docker para Machine Learning

Explique:

- image;
- container;
- Dockerfile;
- layers;
- volumes;
- networks;
- environment variables;
- multi-stage builds.

Mostre como containerizar treinamento e inferência.

---

## 25. Docker Compose

Mostre uma arquitetura local com:

```text
API
Model Service
Database
MLflow
Object Storage
```

Explique comunicação entre os componentes.

---

## 26. Kubernetes

Introduza:

- pod;
- deployment;
- service;
- ingress;
- configmap;
- secret;
- autoscaling;
- resource requests;
- resource limits.

Explique por que Kubernetes aparece em sistemas de ML.

Não presuma que todo projeto precisa de Kubernetes.

---

# PARTE VII — MLOPS

## 27. O que é MLOps?

Explique:

- CI;
- CD;
- CT;
- model lifecycle;
- automation;
- reproducibility;
- governance.

---

## 28. CI/CD para Machine Learning

Explique pipelines:

```text
Commit
 ↓
Tests
 ↓
Lint
 ↓
Build
 ↓
Train/Evaluate
 ↓
Register
 ↓
Deploy
```

Discuta quando treinar modelos durante CI/CD e quando não fazê-lo.

---

## 29. Continuous Training

Explique:

- triggers;
- scheduled retraining;
- data-driven retraining;
- validation gates;
- model promotion.

---

## 30. MLflow

Utilize como exemplo de plataforma para:

- experiment tracking;
- artifacts;
- model registry.

Não trate a ferramenta como objetivo final. Explique os conceitos independentes da ferramenta.

---

## 31. Orquestração

Explique Airflow e conceitos de:

- DAG;
- task;
- dependency;
- scheduler;
- retry;
- backfill;
- idempotência.

Mostre uma pipeline de treinamento.

---

# PARTE VIII — SISTEMAS DISTRIBUÍDOS

## 32. Fundamentos

Explique:

- processos;
- threads;
- concorrência;
- paralelismo;
- comunicação entre serviços;
- filas;
- workers.

---

## 33. Processamento distribuído

Explique:

- particionamento;
- shuffling;
- fault tolerance;
- distributed computation.

Introduza Apache Spark.

---

## 34. Sistemas assíncronos

Explique:

- message queues;
- producers;
- consumers;
- workers;
- retries;
- dead-letter queues;
- idempotência.

Relacione isso com inferência e pipelines de ML.

---

## 35. Escalabilidade

Explique:

- horizontal scaling;
- vertical scaling;
- load balancing;
- autoscaling;
- bottlenecks.

Mostre como escalar uma API de inferência.

---

# PARTE IX — OBSERVABILIDADE

## 36. Observabilidade em ML

Explique:

- logs;
- metrics;
- traces.

Depois introduza métricas específicas de ML.

---

## 37. Data monitoring

Explique:

- schema drift;
- data drift;
- distribution drift;
- missing values;
- feature anomalies.

---

## 38. Model monitoring

Explique:

- performance degradation;
- concept drift;
- prediction drift;
- calibration;
- business metrics.

---

## 39. Alerting

Mostre como definir:

- thresholds;
- alerts;
- severity;
- escalation;
- incident response.

---

# PARTE X — PRODUÇÃO E CONFIABILIDADE

## 40. Reliability

Explique:

- availability;
- reliability;
- fault tolerance;
- retries;
- timeouts;
- circuit breakers;
- graceful degradation.

---

## 41. Deployment strategies

Explique:

- rolling deployment;
- blue-green;
- canary;
- shadow deployment;
- rollback.

Mostre quando cada estratégia é apropriada.

---

## 42. Segurança

Aborde:

- secrets;
- authentication;
- authorization;
- API security;
- dependency vulnerabilities;
- container security;
- data protection.

---

## 43. Custos

Explique:

- compute;
- storage;
- network;
- inference cost;
- GPU cost;
- training cost.

Mostre como custo entra nas decisões arquiteturais.

---

# PARTE XI — CLOUD

## 44. Cloud para ML Engineering

Apresente os conceitos comuns às principais clouds:

- compute;
- object storage;
- databases;
- container registry;
- Kubernetes;
- managed ML;
- monitoring.

Não transforme a apostila em um tutorial específico de uma única cloud.

---

## 45. Arquitetura cloud-native

Mostre uma arquitetura completa:

```text
Data Sources
     ↓
Object Storage
     ↓
Data Pipeline
     ↓
Feature/Data Store
     ↓
Training Pipeline
     ↓
Model Registry
     ↓
Deployment
     ↓
Inference Service
     ↓
Monitoring
     ↓
Retraining
```

Explique cada componente.

---

# PARTE XII — LLM / GENERATIVE AI ENGINEERING

Inclua uma seção moderna sobre sistemas de IA generativa.

## 46. LLM Engineering

Aborde:

- tokens;
- embeddings;
- inference;
- context windows;
- prompt management;
- structured outputs.

---

## 47. RAG

Explique:

```text
Documents
 ↓
Chunking
 ↓
Embeddings
 ↓
Vector Store
 ↓
Retrieval
 ↓
Context
 ↓
LLM
 ↓
Response
```

Aborde:

- chunking;
- retrieval;
- reranking;
- vector databases;
- evaluation;
- hallucination.

---

## 48. LLM Evaluation

Explique:

- factuality;
- relevance;
- groundedness;
- latency;
- cost;
- automated evaluation;
- human evaluation.

---

## 49. Agents

Explique:

- tool calling;
- planning;
- memory;
- state;
- orchestration;
- observability;
- failure modes.

---

# PARTE XIII — MACHINE LEARNING SYSTEM DESIGN

Esta parte deve ser uma das mais importantes da apostila.

## 50. Como projetar um sistema de ML

Ensine um método sistemático:

1. definir o problema;
2. definir métricas;
3. entender os dados;
4. estimar escala;
5. definir requisitos;
6. escolher arquitetura;
7. definir treinamento;
8. definir serving;
9. definir monitoramento;
10. definir estratégia de evolução.

---

## 51. Trade-offs

Discuta:

- accuracy vs latency;
- accuracy vs cost;
- batch vs online;
- CPU vs GPU;
- monolith vs microservices;
- managed vs self-hosted;
- real-time vs eventual consistency.

---

## 52. Estudos de caso

Inclua estudos de caso como:

- sistema de recomendação;
- detecção de fraude;
- previsão de demanda;
- classificação de documentos;
- ranking;
- churn prediction;
- sistema de busca;
- RAG.

Para cada caso, apresente:

```text
Requirements
Data
Model
Training
Serving
Infrastructure
Monitoring
Scaling
Failure Modes
Trade-offs
```

---

# PARTE XIV — PROJETOS PRÁTICOS

A apostila deve terminar com projetos progressivos.

## Projeto 1 — Modelo local

Construir:

```text
Dataset
 ↓
Training
 ↓
Evaluation
 ↓
Model Artifact
```

---

## Projeto 2 — ML API

Construir:

```text
Model
 ↓
FastAPI
 ↓
Docker
```

Adicionar:

- validation;
- tests;
- logging;
- health checks.

---

## Projeto 3 — Training Pipeline

Construir:

```text
Data
 ↓
Validation
 ↓
Training
 ↓
Evaluation
 ↓
Model Registry
```

Utilizar MLflow.

---

## Projeto 4 — Pipeline orquestrado

Adicionar Airflow.

---

## Projeto 5 — Sistema completo

Construir uma arquitetura contendo:

- PostgreSQL;
- object storage;
- data pipeline;
- training pipeline;
- MLflow;
- FastAPI;
- Docker;
- monitoring;
- orchestration.

---

## Projeto 6 — Sistema distribuído

Adicionar:

- queue;
- workers;
- asynchronous inference;
- horizontal scaling.

---

## Projeto 7 — Projeto de portfólio

Criar um sistema completo de ML Engineering com aparência de projeto profissional.

O projeto deve possuir:

- arquitetura documentada;
- README;
- diagramas;
- testes;
- CI;
- Docker;
- observabilidade;
- pipelines;
- deployment;
- documentação de API;
- decisões arquiteturais;
- métricas;
- benchmarks.

---

# PARTE XV — ENTREVISTAS E COMPETÊNCIAS PROFISSIONAIS

Inclua uma seção voltada para preparação profissional.

Explique o que um candidato deve saber sobre:

- Python;
- SQL;
- Linux;
- Git;
- APIs;
- Docker;
- cloud;
- ML;
- data engineering;
- MLOps;
- distributed systems;
- system design.

Inclua perguntas de entrevista:

### Fundamentos

### Python

### ML

### Data Engineering

### MLOps

### Docker

### Kubernetes

### System Design

### ML System Design

### LLM Engineering

Para cada pergunta, forneça:

- resposta curta;
- explicação profunda;
- armadilhas comuns;
- follow-up provável do entrevistador.

---

# PARTE XVI — GLOSSÁRIO

Finalize com um glossário técnico contendo termos como:

- inference;
- serving;
- drift;
- feature store;
- model registry;
- artifact;
- lineage;
- orchestration;
- idempotency;
- observability;
- throughput;
- latency;
- P95;
- P99;
- training-serving skew;
- data leakage;
- concept drift;
- batch inference;
- online inference;
- canary deployment;
- shadow deployment;
- etc.

---

# 5. PADRÃO DE CÓDIGO

Os exemplos devem ser profissionais.

Priorize:

- Python moderno;
- type hints;
- funções pequenas;
- módulos bem definidos;
- testes;
- tratamento de erros;
- configuração externa;
- logging.

Quando apropriado, utilize:

- FastAPI;
- Pydantic;
- pytest;
- Docker;
- PostgreSQL;
- MLflow;
- Airflow;
- PySpark;
- Redis;
- ferramentas de observabilidade.

Não introduza ferramentas apenas para aumentar a quantidade de tecnologias.

Explique sempre:

> "Qual problema essa ferramenta resolve?"

e:

> "Eu realmente preciso dela?"

---

# 6. ARQUITETURA DOS EXEMPLOS

Sempre que apresentar um sistema relevante, mostre primeiro uma arquitetura conceitual.

Exemplo:

```text
                ┌──────────────┐
                │ Data Sources │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Data Pipeline│
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │ Data Storage │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │Training       │
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │Model Registry│
                └──────┬───────┘
                       ↓
                ┌──────────────┐
                │Model Serving │
                └──────┬───────┘
                       ↓
                   Consumers
```

Depois explique cada componente.

---

# 7. TRADE-OFFS E DECISÕES

Não apresente ferramentas ou arquiteturas como universalmente corretas.

Sempre que possível, explique:

| Decisão | Opção A | Opção B | Quando usar |
|---|---|---|---|
| Inferência | Batch | Online | dependendo da latência |
| Storage | SQL | Object Storage | dependendo dos dados |
| Processing | Python | Spark | dependendo da escala |
| Deployment | VM | Container | dependendo da operação |
| Serving | Monolith | Microservice | dependendo da complexidade |
| Compute | CPU | GPU | dependendo do modelo |

O objetivo é ensinar **engenharia de decisão**, não decorar ferramentas.

---

# 8. ERROS E ANTI-PATTERNS

Inclua uma seção de "Como sistemas de ML dão errado".

Exemplos:

- notebook indo diretamente para produção;
- treinamento manual;
- datasets sem versionamento;
- ausência de testes;
- data leakage;
- feature skew;
- ausência de monitoramento;
- modelo sem rollback;
- pipelines não idempotentes;
- dependências não fixadas;
- modelo incompatível com ambiente;
- overengineering;
- Kubernetes sem necessidade;
- microservices prematuros;
- monitorar apenas CPU/memória;
- monitorar apenas accuracy;
- ignorar métricas de negócio.

Explique por que cada prática é problemática.

---

# 9. MATURIDADE

Crie um modelo de maturidade:

### Nível 0 — Notebook

Experimentos manuais.

### Nível 1 — Script

Código organizado e reproduzível.

### Nível 2 — Pipeline

Training e data pipelines automatizados.

### Nível 3 — Production ML

Serving, registry e monitoramento.

### Nível 4 — MLOps

CI/CD/CT, observabilidade e automação.

### Nível 5 — ML Platform

Infraestrutura reutilizável para múltiplos times.

Explique como uma empresa evolui entre esses níveis.

---

# 10. PROBLEMAS DE PRODUÇÃO

Inclua cenários realistas.

Exemplo:

> O modelo apresenta 94% de accuracy durante avaliação, mas sua performance caiu em produção.

O leitor deve investigar:

- data drift;
- concept drift;
- pipeline quebrado;
- mudança de distribuição;
- training-serving skew;
- alteração de comportamento do usuário;
- bugs;
- mudanças externas.

Inclua diversos incidentes desse tipo e explique como investigá-los.

---

# 11. SYSTEM DESIGN

Inclua exercícios de design.

Exemplos:

> Projete um sistema de recomendação para 10 milhões de usuários.

> Projete uma API de fraude com latência inferior a 100 ms.

> Projete uma plataforma de treinamento para dezenas de modelos.

> Projete um sistema de previsão de demanda.

> Projete um RAG corporativo.

Para cada exercício, ensine a estruturar a resposta.

---

# 12. RIGOR TÉCNICO

Não invente conceitos, ferramentas ou comportamentos de sistemas.

Quando houver diferentes abordagens, apresente as alternativas.

Diferencie claramente:

- fato;
- prática recomendada;
- heurística;
- trade-off;
- opinião arquitetural.

Quando uma tecnologia ou prática mudar rapidamente, indique que ela é dependente de versão/ecossistema e, quando necessário, utilize documentação atualizada.

---

# 13. REFERÊNCIAS

Ao final de cada grande parte, indique referências de alta qualidade:

- documentação oficial;
- livros;
- papers;
- artigos técnicos;
- documentação de ferramentas;
- materiais acadêmicos.

Priorize fontes primárias.

Não transforme a apostila em uma coleção de links. As referências devem complementar o conteúdo.

---

# 14. FORMATO

Produza a apostila em Markdown.

Utilize:

- títulos hierárquicos;
- diagramas ASCII;
- tabelas quando realmente ajudarem;
- blocos de código;
- exemplos;
- exercícios;
- estudos de caso;
- checklists.

Não transforme cada pequeno conceito em uma seção artificial.

O texto deve parecer uma **apostila técnica profissional**, não uma sequência de posts de blog.

---

# 15. PROFUNDIDADE

A apostila deve ser extensa.

Não tente reduzir o conteúdo para economizar tokens.

Quando um assunto for fundamental para Machine Learning Engineering, explique profundamente.

Especialmente:

- software engineering;
- data pipelines;
- reproducibility;
- training pipelines;
- model serving;
- Docker;
- MLOps;
- orchestration;
- observability;
- distributed systems;
- ML system design.

O leitor deve terminar a apostila entendendo não apenas "como fazer", mas **por que a arquitetura funciona e quais problemas aparecem quando ela cresce**.

---

# 16. REGRA FUNDAMENTAL

Ao explicar qualquer tecnologia, ferramenta ou arquitetura, sempre responda às cinco perguntas:

1. **Qual problema isso resolve?**
2. **Como funciona internamente?**
3. **Como é utilizado em um sistema de ML?**
4. **Quais são os trade-offs?**
5. **Quando eu não deveria utilizar isso?**

O objetivo não é formar um usuário de ferramentas.

O objetivo é formar um **Machine Learning Engineer capaz de projetar, implementar, operar e evoluir sistemas de Machine Learning em produção.**

---

# RESULTADO ESPERADO

Ao terminar a apostila, o leitor deverá conseguir:

- desenvolver modelos de ML;
- estruturar projetos profissionais;
- criar pipelines de dados;
- criar pipelines de treinamento;
- versionar experimentos e modelos;
- construir APIs de inferência;
- containerizar aplicações;
- automatizar workflows;
- utilizar orquestração;
- implementar observabilidade;
- monitorar dados e modelos;
- compreender sistemas distribuídos;
- escalar inferência;
- projetar arquiteturas de ML;
- avaliar trade-offs;
- trabalhar com cloud;
- trabalhar com MLOps;
- construir sistemas de LLM/RAG;
- diagnosticar problemas de produção;
- discutir ML System Design em entrevistas;
- construir projetos de portfólio próximos de ambientes profissionais.

A prioridade deve ser **profundidade, conexão entre conceitos e raciocínio de engenharia**, e não simplesmente quantidade de tecnologias apresentadas.