# 清除和控制

> 实际数据是我所发现的, 错误的模特是我学会的.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## 学习目标

- 检测缺失的值 (中,中,模式) 作为熊猫
- 规范类型,手动删除重复字符串
- 皮尔森的计算对比率为零和数量对比矩阵
- 总体报告 可复制的最低

## 问题

据估计,科学家的步伐在80%上是清洁的.`""`现在`"N/A"`现在`"null"`模特不配合被遗弃的废物,它们被扩大.

## 概念

### 缺失:类型

-         
-                   
-                                                                                                                                                                                                                                                               

战略:移除线,媒体/中介/moda,近距离.

### 皮尔森的关系

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
只有捕捉线性关系.

```mermaid
flowchart LR
    A[CSV bruto] --> B[Parse tipos]
    B --> C[Missing?]
    C --> D[Imputar / Remover]
    D --> E[Duplicatas]
    E --> F[Padronizar]
    F --> G[Correlação]
    G --> H[Relatório EDA]
```

```figure
eda-pipeline
```

## 建立它

### 步骤1:检查并检测失踪

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### 步骤2: 起

```python
def impute(rows, col, strategy="median"):
    vals = [float(r[col]) for r in rows if not is_missing(r[col])]
    vals.sort()
    if strategy == "mean":
        fill = sum(vals)/len(vals)
    elif strategy == "median":
        fill = vals[len(vals)//2]
    else: # mode
        fill = max(set(vals), key=vals.count)
    for r in rows:
        if is_missing(r[col]):
            r[col] = fill
    return fill
```

### 步骤3: 相关性

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## 用它

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## 运送它

`outputs/skill-limpeza-eda.md`可再生的管道.

## 运动

1. 实施人数单位 (例如:部门薪资中位).
2. 检测复制品的复制品.
3. 比较皮尔森与斯皮尔曼的数据.

## 关键词

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## 进一步阅读

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
