---
name: skill-limpeza-eda
description: Pipeline reprodutível de limpeza e EDA
phase: 20
lesson: 02
tags: [cleaning, eda, pandas]
---

# Skill — Limpeza e EDA

1. Detectar missing com lista `["", "N/A", "null"]`.
2. Imputar: mediana se assimétrico, média se simétrico, moda para categórico.
3. Deduplicar por chave.
4. Correlação Pearson para pares numéricos; alertar se |r|>0.9 (multicolinearidade).
5. Gerar relatório: % missing, % dup, matriz correlação.
