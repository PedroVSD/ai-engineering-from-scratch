---
name: skill-reprodutibilidade-tracking
description: Checklist para experimentos reproduzíveis com tracking JSONL
phase: 20
lesson: 9
tags: [reprodutibilidade, seeds, tracking, mlflow]
---

# Skill — Reprodutibilidade e Tracking

Use no início de todo experimento:

1. Fixe e registre a seed (`set_seed(42)`); use `Random(seed)` local em splits.
2. Versione o dataset: `dataset_hash()` SHA-256 do JSON canônico.
3. Um config dict por run: todos os hiperparâmetros explícitos.
4. Um JSON por run em `.jsonl`: timestamp + seed + dataset_hash + params + metrics.
5. Compare com `best_run(runs, metric)` — nunca escolha "de olho".
6. Produção: mesmo contrato no mlflow (`log_params` + `log_metric` + dataset hash).
