---
name: skill-clean-code-ds
description: Checklist para converter notebook em pipeline testável
phase: 20
lesson: 8
tags: [clean-code, testes, data-quality, schema]
---

# Skill — Clean Code para DS

Use ao converter qualquer notebook em código de produção:

1. Uma função = um verbo (`validate`, `clean`, `featurize`); I/O só nas bordas.
2. Funções puras: parâmetros explícitos, retorno novo, zero global.
3. Valide o schema na entrada; erro deve dizer linha + coluna + valor.
4. Quality checks nomeados: `sem_nulos`, `idades_validas`, `sem_duplicatas`.
5. Pirâmide: muitos unitários/schema rápidos, poucos e2e lentos.
6. Nunca mute o input — `{**r}` em vez de `r[col] = ...`.
