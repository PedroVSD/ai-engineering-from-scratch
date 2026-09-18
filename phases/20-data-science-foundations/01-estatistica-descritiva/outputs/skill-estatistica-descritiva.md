---
name: skill-estatistica-descritiva
description: Checklist de EDA descritivo antes de modelar
phase: 20
lesson: 01
tags: [eda, estatistica, iqr, z-score]
---

# Skill — Estatística Descritiva

Use antes de qualquer modelo:

1. Reporte média E mediana; se diferirem >20%, use mediana.
2. Reporte desvio E IQR; prefira IQR se |skew|>1.
3. Histograma (5-10 bins) + boxplot.
4. % outliers por IQR (k=1.5) e por |z|>3 — compare.
5. Se |z|max > 5 e distribuição assimétrica, não use z-score.
