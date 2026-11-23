# Limpeza e EDA انجام صفر

> اطلاعات واقعی که در مورد آن ها می بینید گم شده است، دوگونی شده و انواع قبل از اینکه مدل یاد گرفته یا اشتباه کرده باشد.

**Type:** Build
**Languages:** Python
**Prerequisites:** 01-estatistica-descritiva
**Time:** ~70 minutes

## اهداف یادگیری

- تشخیص و تشخیص ارزش های غیبی (میدیا، مدانا، مودا) در پاندا
- انواع نرمال سازی، حذف کپی ها و استاندارد سازی رشته ها به صورت دستی
- محاسبه ارتباط پیرسون صفر و ماتر ماتر ارتباط
- گزارش GERAR um relatório EDA حداقل قابل تکرار

## مشکل

در واقع 80 درصد از سرعت یک دانشمند در حال پاک شدن است.`""`،`"N/A"`،`"null"`مدل های ساخته شده در حال بازپسین و در حال افزایش هستند.

## مفهوم

### گمشده: انواع

- MCAR (perda aleatória)  imputar ok
- MAR (perda depende de outro campo)  شرط بندی شده
- MNAR (حساس از دست دادن به ارزش خود) 

استراتژی ها: حذف linha, média/mediana/moda, vizinho mais próximo.

### ارتباط پیرسون

```
r = cov(X,Y) / (std(X)*std(Y))
cov = mean((x - mx)(y - my))
```
r=1 correlação perfeita, 0 nenhuma, -1 برعکس.

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

## آن را بسازید

### مرحله ی اول: بررسی و تشخیص گمشده

```python
def is_missing(v):
    return v is None or str(v).strip().lower() in ("", "na", "n/a", "null", "none", "-")

def column_stats(rows, col):
    vals = [r[col] for r in rows if not is_missing(r[col])]
    nums = [float(v) for v in vals]
    return len(vals), sum(nums)/len(nums) if nums else None
```

### مرحله دوم: فرض

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

### مرحله سوم: ارتباط

```python
def pearson(x, y):
    mx, my = sum(x)/len(x), sum(y)/len(y)
    num = sum((a-mx)*(b-my) for a,b in zip(x,y))
    den = (sum((a-mx)**2 for a in x)*sum((b-my)**2 for b in y))**0.5
    return num/den if den else 0
```

## ازش استفاده کن

```python
import pandas as pd
df = pd.read_csv("data.csv", na_values=["", "N/A", "null"])
print(df.isna().sum())
df["idade"] = df["idade"].fillna(df["idade"].median())
print(df.corr(numeric_only=True))
```

## -باده

`outputs/skill-limpeza-eda.md` لامپ های تولید مجدد

## تمرینات

1. Implement imputação per grupo (به عنوان مثال: متوسط حقوق در بخش)
2. اضافه کردن دو نسخه از مواد شیمیایی
3. مقایسه پیرسون و اسپیرمن در نظر گرفتن کاموتر چیست؟

## اصطلاحات کلیدی

| Term | O que é |
|---|---|
| MCAR | Missing completamente aleatório |
| Imputação | Preencher faltantes com estatística |
| Pearson | Correlação linear [-1,1] |
| EDA | Análise exploratória antes de modelar |

## خواندن بیشتر

- [Pandas missing data guide](https://pandas.pydata.org/docs/user_guide/missing_data.html)
- [Hadley Wickham — Tidy Data](https://vita.had.co.nz/papers/tidy-data.pdf)
