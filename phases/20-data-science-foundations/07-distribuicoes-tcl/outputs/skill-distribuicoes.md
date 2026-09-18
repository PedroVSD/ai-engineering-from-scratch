---
name: skill-distribuicoes
description: Escolher a distribuição certa e saber quando o TCL autoriza intervalo normal
phase: 20
lesson: 07
tags: [distribuicoes, tcl, binomial, poisson, normal]
---

# Skill — Distribuições

Qual modelo usar:

1. 0/1 único → Bernoulli(p). k sucessos em n → Binomial(n,p).
2. Contagem de raros por intervalo → Poisson(λ), E=Var=λ.
3. Tempo entre eventos → Exponencial(λ), E=1/λ.
4. Medida simétrica com erro aditivo → Normal(μ,σ), 68-95-99.7.
5. Precisa de IC para a média? Se n≥30 e Var finita, TCL: X̄ ± 1.96·σ/√n.
6. Caudas pesadas (Cauchy-like)? TCL não vale — use bootstrap/mediana.
