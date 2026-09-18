import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m

def test_regression_recovers_weights():
    X = [i / 10 for i in range(20)]
    y = [2 * x + 5 for x in X]
    model = m.LinearRegression(lr=0.1)
    model.fit(X, y, epochs=1000)
    assert abs(model.w - 2) < 0.15
    assert abs(model.b - 5) < 0.5

def test_r2_perfect():
    model = m.LinearRegression()
    model.w, model.b = 2, 0
    assert abs(model.r2([1,2,3],[2,4,6]) - 1.0) < 1e-9

def test_mse():
    model = m.LinearRegression()
    model.w, model.b = 1, 0
    assert model.mse([1,2],[1,2]) == 0

def test_predict():
    model = m.LinearRegression()
    model.w, model.b = 2, 1
    assert model.predict([1,2]) == [3,5]
