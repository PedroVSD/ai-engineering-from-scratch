import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))
import main as m

def test_is_missing():
    assert m.is_missing("") and m.is_missing("N/A") and m.is_missing(None)
    assert not m.is_missing("42")

def test_impute_median():
    rows = [{"a": "1"}, {"a": ""}, {"a": "3"}]
    m.impute(rows, "a", "median")
    assert float(rows[1]["a"]) == 2.0

def test_dedup():
    rows = [{"x": "1"}, {"x": "1"}, {"x": "2"}]
    assert len(m.deduplicate(rows)) == 2

def test_pearson_perfect():
    assert abs(m.pearson([1,2,3],[2,4,6]) - 1.0) < 1e-9

def test_pearson_zero():
    assert abs(m.pearson([1,2,3],[1,1,1])) < 1e-9

def test_correlation_matrix():
    mat = m.correlation_matrix({"a":[1,2,3],"b":[1,2,3]})
    assert mat[("a","a")] == 1.0
