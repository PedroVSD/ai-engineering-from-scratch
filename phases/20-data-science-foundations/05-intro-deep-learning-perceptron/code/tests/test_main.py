import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m

def test_perceptron_and():
    X=[[0,0],[0,1],[1,0],[1,1]]
    y=[0,0,0,1]
    p=m.Perceptron(2, lr=0.1)
    p.fit(X,y, epochs=10)
    assert p.predict(X)==y

def test_perceptron_xor_fails():
    X=[[0,0],[0,1],[1,0],[1,1]]
    y=[0,1,1,0]
    p=m.Perceptron(2)
    p.fit(X,y, epochs=20)
    acc=sum(a==b for a,b in zip(y,p.predict(X)))/4
    assert acc < 1.0

def test_mlp_xor():
    X=[[0,0],[0,1],[1,0],[1,1]]
    y=[0,1,1,0]
    mlp=m.MLP(n_hidden=8, lr=0.1)
    mlp.fit(X,y, epochs=8000)
    acc=sum(a==b for a,b in zip(y,mlp.predict(X)))/4
    assert acc == 1.0

def test_relu():
    assert m.relu(-1)==0 and m.relu(2)==2
    assert m.relu_deriv(1)==1 and m.relu_deriv(-1)==0
