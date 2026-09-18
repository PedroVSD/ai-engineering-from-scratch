---
name: skill-probabilidade
description: Inverter condicionais com Bayes sem cair na falácia da taxa-base
phase: 20
lesson: 06
tags: [probabilidade, bayes, condicional, taxa-base]
---

# Skill — Probabilidade

Antes de concluir qualquer "P(X|evidência)":

1. Declare o prior P(X) — sem prior, sem posterior.
2. Declare a verossimilhança P(evidência|X) e a taxa de falso-positivo.
3. Calcule a evidência P(evidência) pela lei total.
4. Posterior = verossimilhança × prior / evidência.
5. Sanity check: classe rara + teste imperfeito → posterior baixo mesmo com positivo.
