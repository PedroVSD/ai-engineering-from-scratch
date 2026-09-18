# phases/20-data-science-foundations/09-reprodutibilidade-tracking/code/main.py
# Lesson: Reprodutibilidade e Tracking de Experimentos — docs/en.md
# Spec: seeds, sha256 dataset versioning, JSONL experiment tracker (stdlib only)

import datetime
import hashlib
import json
import random
import tempfile
from pathlib import Path

DATASET = [{"x": i, "y": 2 * i + 1} for i in range(20)]
DEFAULT_SEED = 42


def set_seed(seed):
    """Fix the global random seed. Returns the seed for logging."""
    random.seed(seed)
    return seed


def train_test_split(rows, test_ratio=0.2, seed=DEFAULT_SEED):
    """Deterministic split using a local RNG (does not touch global state)."""
    rng = random.Random(seed)
    idx = list(range(len(rows)))
    rng.shuffle(idx)
    k = int(len(rows) * (1 - test_ratio))
    return [rows[i] for i in idx[:k]], [rows[i] for i in idx[k:]]


def dataset_hash(rows):
    """Short SHA-256 version of the canonical JSON of rows."""
    canon = json.dumps(rows, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(canon.encode("utf-8")).hexdigest()[:12]


def train_mean_predictor(train_rows):
    """Toy model: predict mean(y) of train. Returns params dict."""
    mean_y = sum(r["y"] for r in train_rows) / len(train_rows)
    return {"mean_y": mean_y}


def evaluate_mae(model, test_rows):
    """Mean absolute error of the mean predictor."""
    return sum(abs(r["y"] - model["mean_y"]) for r in test_rows) / len(test_rows)


def log_run(path, params, metrics, seed, dhash):
    """Append one JSON record per run. Returns the record."""
    record = {
        "timestamp": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "seed": seed,
        "dataset_hash": dhash,
        "params": params,
        "metrics": metrics,
    }
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(record, ensure_ascii=False) + "\n")
    return record


def load_runs(path):
    """Load all run records from a JSONL file."""
    with open(path, encoding="utf-8") as f:
        return [json.loads(line) for line in f if line.strip()]


def best_run(runs, metric="mae", higher=False):
    """Pick best run by metric. Pure function."""
    pick = max if higher else min
    return pick(runs, key=lambda r: r["metrics"][metric])


def run_experiment(rows, seed, test_ratio, path):
    """Full experiment: split, train, evaluate, log. Returns record."""
    train, test = train_test_split(rows, test_ratio=test_ratio, seed=seed)
    model = train_mean_predictor(train)
    mae = evaluate_mae(model, test)
    return log_run(
        path,
        params={"test_ratio": test_ratio, "model": "mean"},
        metrics={"mae": mae},
        seed=seed,
        dhash=dataset_hash(rows),
    )


def main():
    print("=== Reprodutibilidade + Tracking ===")
    set_seed(DEFAULT_SEED)
    dhash = dataset_hash(DATASET)
    print(f"dataset n={len(DATASET)} hash={dhash}")
    train, test = train_test_split(DATASET, seed=DEFAULT_SEED)
    print(f"split seed={DEFAULT_SEED}: train={len(train)} test={len(test)}")

    tmp = Path(tempfile.gettempdir()) / "runs_demo.jsonl"
    if tmp.exists():
        tmp.unlink()
    for ratio in (0.2, 0.3):
        rec = run_experiment(DATASET, seed=DEFAULT_SEED, test_ratio=ratio, path=str(tmp))
        print(f"  run test_ratio={ratio} mae={rec['metrics']['mae']:.3f}")
    runs = load_runs(str(tmp))
    best = best_run(runs, metric="mae", higher=False)
    print(f"melhor run: test_ratio={best['params']['test_ratio']} mae={best['metrics']['mae']:.3f}")
    print(f"log em {tmp} ({len(runs)} runs)")
    print("OK — experimento reproduzivel registrado.")


if __name__ == "__main__":
    main()
