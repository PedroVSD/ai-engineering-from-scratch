# phases/20-data-science-foundations/03-regressao-do-zero/code/main.py
# Lesson: Regressão Linear do Zero

import random
import math


class LinearRegression:
    def __init__(self, lr=0.01):
        self.w = 0.0
        self.b = 0.0
        self.lr = lr

    def predict(self, X):
        return [self.w * x + self.b for x in X]

    def mse(self, X, y):
        preds = self.predict(X)
        return sum((p - a) ** 2 for p, a in zip(preds, y)) / len(y)

    def fit(self, X, y, epochs=800):
        for _ in range(epochs):
            preds = self.predict(X)
            n = len(y)
            dw = (2 / n) * sum((p - a) * x for p, a, x in zip(preds, y, X))
            db = (2 / n) * sum(p - a for p, a in zip(preds, y))
            self.w -= self.lr * dw
            self.b -= self.lr * db
        return self

    def r2(self, X, y):
        preds = self.predict(X)
        y_mean = sum(y) / len(y)
        ss_res = sum((a - p) ** 2 for a, p in zip(y, preds))
        ss_tot = sum((a - y_mean) ** 2 for a in y)
        return 1 - ss_res / ss_tot if ss_tot else 0


def main():
    random.seed(0)
    X = [random.uniform(0, 10) for _ in range(100)]
    y = [3 * x + 7 + random.gauss(0, 2) for x in X]

    # split 80/20
    n_train = 80
    X_train, X_test = X[:n_train], X[n_train:]
    y_train, y_test = y[:n_train], y[n_train:]

    model = LinearRegression(lr=0.02)
    model.fit(X_train, y_train, epochs=600)
    print(f"w={model.w:.3f} b={model.b:.3f} (true w=3 b=7)")
    print(f"train R2={model.r2(X_train, y_train):.3f} test R2={model.r2(X_test, y_test):.3f} MSE={model.mse(X_test, y_test):.3f}")

    # Normal equation
    x_mean = sum(X_train) / len(X_train)
    y_mean = sum(y_train) / len(y_train)
    num = sum((x - x_mean) * (yy - y_mean) for x, yy in zip(X_train, y_train))
    den = sum((x - x_mean) ** 2 for x in X_train)
    w_closed = num / den if den else 0
    b_closed = y_mean - w_closed * x_mean
    print(f"[normal] w={w_closed:.3f} b={b_closed:.3f}")

    try:
        from sklearn.linear_model import LinearRegression as SkLR
        import numpy as np
        Xt = np.array(X_train).reshape(-1, 1)
        Xe = np.array(X_test).reshape(-1, 1)
        sk = SkLR().fit(Xt, y_train)
        print(f"[sklearn] w={sk.coef_[0]:.3f} b={sk.intercept_:.3f} R2={sk.score(Xe, y_test):.3f}")
    except ImportError:
        print("sklearn não instalado — pulado")

    print("OK — regressão validada.")


if __name__ == "__main__":
    main()
