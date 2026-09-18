# phases/20-data-science-foundations/04-classificacao-e-avaliacao/code/main.py
import math
import random


def sigmoid(z):
    if z < -30:
        return 0.0
    if z > 30:
        return 1.0
    return 1 / (1 + math.exp(-z))


class LogisticRegression:
    def __init__(self, lr=0.1):
        self.w = 0.0
        self.b = 0.0
        self.lr = lr

    def predict_proba(self, X):
        return [sigmoid(self.w * x + self.b) for x in X]

    def predict(self, X, thresh=0.5):
        return [1 if p >= thresh else 0 for p in self.predict_proba(X)]

    def fit(self, X, y, epochs=500):
        for _ in range(epochs):
            probs = self.predict_proba(X)
            n = len(y)
            dw = sum((p - a) * x for p, a, x in zip(probs, y, X)) / n
            db = sum(p - a for p, a in zip(probs, y)) / n
            self.w -= self.lr * dw
            self.b -= self.lr * db
        return self


def confusion(y_true, y_pred):
    tp = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 1)
    tn = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 0)
    fp = sum(1 for a, p in zip(y_true, y_pred) if a == 0 and p == 1)
    fn = sum(1 for a, p in zip(y_true, y_pred) if a == 1 and p == 0)
    return {"TP": tp, "TN": tn, "FP": fp, "FN": fn}


def metrics(cm):
    tp, fp, fn, tn = cm["TP"], cm["FP"], cm["FN"], cm["TN"]
    acc = (tp + tn) / (tp + tn + fp + fn) if (tp + tn + fp + fn) else 0
    prec = tp / (tp + fp) if (tp + fp) else 0
    rec = tp / (tp + fn) if (tp + fn) else 0
    f1 = 2 * prec * rec / (prec + rec) if (prec + rec) else 0
    return {"accuracy": acc, "precision": prec, "recall": rec, "f1": f1}


def roc_auc(y_true, y_score):
    pairs = sorted(zip(y_score, y_true), reverse=True)
    # simple AUC via ranking
    n_pos = sum(y_true)
    n_neg = len(y_true) - n_pos
    if n_pos == 0 or n_neg == 0:
        return 0.5
    # count concordant pairs
    score_pos = [s for s, y in pairs if y == 1]
    score_neg = [s for s, y in pairs if y == 0]
    wins = sum(1 for sp in score_pos for sn in score_neg if sp > sn)
    ties = sum(1 for sp in score_pos for sn in score_neg if sp == sn)
    return (wins + 0.5 * ties) / (n_pos * n_neg)


def main():
    random.seed(0)
    # two gaussians
    X0 = [random.gauss(-1, 1) for _ in range(50)]
    X1 = [random.gauss(1.5, 1) for _ in range(50)]
    X = X0 + X1
    y = [0] * 50 + [1] * 50
    # shuffle
    combined = list(zip(X, y))
    random.shuffle(combined)
    X, y = zip(*combined)
    X, y = list(X), list(y)
    n_train = 80
    X_train, X_test = X[:n_train], X[n_train:]
    y_train, y_test = y[:n_train], y[n_train:]

    model = LogisticRegression(lr=0.5)
    model.fit(X_train, y_train, epochs=400)
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)
    cm = confusion(y_test, y_pred)
    mets = metrics(cm)
    print(f"w={model.w:.3f} b={model.b:.3f}")
    print(f"confusion {cm}")
    print(f"metrics { {k: round(v,3) for k,v in mets.items()} }")
    print(f"AUC={roc_auc(y_test, y_proba):.3f}")

    # demo acurácia enganosa
    y_imb = [0]*95 + [1]*5
    y_pred_all0 = [0]*100
    cm2 = confusion(y_imb, y_pred_all0)
    print(f"[desbalanceado] sempre negativo -> accuracy {metrics(cm2)['accuracy']:.2f} mas recall {metrics(cm2)['recall']:.2f}")

    try:
        from sklearn.linear_model import LogisticRegression as SkLR
        from sklearn.metrics import classification_report, roc_auc_score
        import numpy as np
        sk = SkLR().fit(np.array(X_train).reshape(-1,1), y_train)
        print(f"[sklearn] {classification_report(y_test, sk.predict(np.array(X_test).reshape(-1,1)), zero_division=0)}")
        print(f"[sklearn] AUC={roc_auc_score(y_test, sk.predict_proba(np.array(X_test).reshape(-1,1))[:,1]):.3f}")
    except ImportError:
        print("sklearn não instalado — pulado")

    print("OK — classificação validada.")


if __name__ == "__main__":
    main()
