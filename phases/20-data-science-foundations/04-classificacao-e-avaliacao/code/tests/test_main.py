import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m

def test_sigmoid():
    assert abs(m.sigmoid(0) - 0.5) < 1e-9
    assert m.sigmoid(100) > 0.99

def test_confusion():
    cm = m.confusion([1,0,1,0],[1,0,0,0])
    assert cm["TP"]==1 and cm["FN"]==1

def test_metrics():
    cm={"TP":2,"TN":2,"FP":1,"FN":1}
    mets=m.metrics(cm)
    assert 0 < mets["f1"] < 1

def test_auc_perfect():
    assert abs(m.roc_auc([0,0,1,1],[0.1,0.2,0.8,0.9]) - 1.0) < 1e-9
