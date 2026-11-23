# " ليمبيزا إد "

> البيانات الحقيقية التي أكتشفتها مفقودة، والنسخة والأنواع التي تعلمتها قبل أن تتعلمها.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## أهداف التعلم

- اكتشاف القيم المفقودة (مديا، مديانا، مودا)
- تطبيق النماذج، إزالة النسخ المزدوجة وتطبيق السلاسل يدويا
- حسابات "بيرسون" للصفر والموارد المرتبطة
- إدراج تقرير إدراجات أقل

## المشكلة

يقدر الكاغل 80% من التوقيت العلمي على الانتباه.`""`،`"N/A"`،`"null"`النسخ المزدوجة تتراجع في القمامة.

## المفهوم

### مفقود: نوع

- (مكار) (ألياتوريا)  إعتبار موافقة
- MAR (perda depende de outro campo)  فرضية مشروطة
- (منار) (الخسارة تعتمد على القوة الخاصة)

استراتيجيات: إزالة linha, média/mediana/moda, vizinho mais próximo.

### "كورلاؤون دي بيرسون"

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
r=1 correlação perfeita، 0 nenhuma، -1 العكس.

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

## بناءها

### الخطوة الأولى: البحث عن المفقودين

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### الخطوة الثانية: الإنتساب

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

### الخطوة الثالثة:

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## استخدمها

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## أرسله

`outputs/skill-limpeza-eda.md` خط أنابيب ليبنزا قابل للتنويع

## التمارين

1. تنفيذ التعاملات الجماعية (مثل: متوسطات الأجور بالمنطقة).
2. إضافة للكشف عن النسخ المزدوجة من الكمبوسات
3. مقارنة بين بيرسون vs سبيرمان في بيانات كم أخرج  ما هو أكثر قوة؟

## الشروط الرئيسية

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## المزيد من القراءة

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
