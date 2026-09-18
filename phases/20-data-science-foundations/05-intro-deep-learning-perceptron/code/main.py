# phases/20-data-science-foundations/05-intro-deep-learning-perceptron/code/main.py
# Lesson: Perceptron e Deep Learning do Zero

import math
import random


class Perceptron:
    def __init__(self, n_features, lr=0.1):
        self.w = [0.0] * n_features
        self.b = 0.0
        self.lr = lr

    def predict_one(self, x):
        s = sum(wi * xi for wi, xi in zip(self.w, x)) + self.b
        return 1 if s >= 0 else 0

    def predict(self, X):
        return [self.predict_one(x) for x in X]

    def fit(self, X, y, epochs=20):
        for _ in range(epochs):
            for xi, yi in zip(X, y):
                pred = self.predict_one(xi)
                err = yi - pred
                for j in range(len(self.w)):
                    self.w[j] += self.lr * err * xi[j]
                self.b += self.lr * err
        return self


def relu(z):
    return max(0, z)


def relu_deriv(z):
    return 1 if z > 0 else 0


def sigmoid(z):
    if z < -30:
        return 0.0
    if z > 30:
        return 1.0
    return 1 / (1 + math.exp(-z))


class MLP:
    def __init__(self, n_in=2, n_hidden=8, lr=0.1):
        random.seed(0)
        self.n_hidden = n_hidden
        self.W1 = [[random.uniform(-1, 1) for _ in range(n_in)] for _ in range(n_hidden)]
        self.b1 = [random.uniform(-0.5, 0.5) for _ in range(n_hidden)]
        self.W2 = [random.uniform(-1, 1) for _ in range(n_hidden)]
        self.b2 = random.uniform(-0.5, 0.5)
        self.lr = lr

    def forward(self, x):
        z1 = [sum(self.W1[i][j] * x[j] for j in range(len(x))) + self.b1[i] for i in range(self.n_hidden)]
        h = [relu(z) for z in z1]
        z2 = sum(self.W2[i] * h[i] for i in range(len(h))) + self.b2
        p = sigmoid(z2)
        return z1, h, z2, p

    def fit(self, X, y, epochs=8000):
        for _ in range(epochs):
            for x, target in zip(X, y):
                z1, h, z2, p = self.forward(x)
                d_z2 = p - target
                old_W2 = list(self.W2)
                for i in range(self.n_hidden):
                    self.W2[i] -= self.lr * d_z2 * h[i]
                self.b2 -= self.lr * d_z2
                for i in range(self.n_hidden):
                    d_h = d_z2 * old_W2[i]
                    d_z1 = d_h * relu_deriv(z1[i])
                    for j in range(len(x)):
                        self.W1[i][j] -= self.lr * d_z1 * x[j]
                    self.b1[i] -= self.lr * d_z1
        return self

    def predict(self, X, thresh=0.5):
        return [1 if self.forward(x)[3] >= thresh else 0 for x in X]


def accuracy(y_true, y_pred):
    return sum(a == p for a, p in zip(y_true, y_pred)) / len(y_true)


def main():
    # AND — linearmente separável
    X_and = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_and = [0, 0, 0, 1]
    perc = Perceptron(n_features=2, lr=0.1)
    perc.fit(X_and, y_and, epochs=10)
    print(f"[perceptron AND] w={perc.w} b={perc.b:.2f} acc={accuracy(y_and, perc.predict(X_and)):.2f}")

    # XOR — não linear
    X_xor = [[0, 0], [0, 1], [1, 0], [1, 1]]
    y_xor = [0, 1, 1, 0]
    perc2 = Perceptron(n_features=2, lr=0.1)
    perc2.fit(X_xor, y_xor, epochs=20)
    print(f"[perceptron XOR] acc={accuracy(y_xor, perc2.predict(X_xor)):.2f} (esperado ~0.5, falha)")

    mlp = MLP(n_in=2, n_hidden=8, lr=0.1)
    mlp.fit(X_xor, y_xor, epochs=8000)
    acc = accuracy(y_xor, mlp.predict(X_xor))
    print(f"[MLP XOR] acc={acc:.2f} {'OK' if acc==1.0 else 'treine mais'}")

    # comparação torch se disponível
    try:
        import torch

        torch.manual_seed(0)
        Xt = torch.tensor(X_xor, dtype=torch.float32)
        yt = torch.tensor(y_xor, dtype=torch.float32).unsqueeze(1)
        model = torch.nn.Sequential(torch.nn.Linear(2, 4), torch.nn.ReLU(), torch.nn.Linear(4, 1), torch.nn.Sigmoid())
        opt = torch.optim.SGD(model.parameters(), lr=0.5)
        loss_fn = torch.nn.BCELoss()
        for _ in range(2000):
            opt.zero_grad()
            out = model(Xt)
            loss = loss_fn(out, yt)
            loss.backward()
            opt.step()
        with torch.no_grad():
            pred = (model(Xt) >= 0.5).int().squeeze().tolist()
        print(f"[torch MLP XOR] pred={pred} acc={accuracy(y_xor, pred):.2f}")
    except ImportError:
        print("torch não instalado — comparação pulada (pip install torch)")

    print("OK — perceptron vs MLP validado.")


if __name__ == "__main__":
    main()
