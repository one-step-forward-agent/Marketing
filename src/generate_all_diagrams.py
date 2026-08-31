from __future__ import annotations

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

EXPECTED_FILENAMES = [
    "jtbd-prioritization.png",
    "importance-vs-satisfaction.png",
    "underserved-jobs.png",
    "overserved-jobs.png",
    "opportunity-map.png",
    "solution-job-fit.png",
]


def _save(fig: plt.Figure, path: Path) -> Path:
    fig.tight_layout()
    fig.savefig(path, dpi=150, bbox_inches="tight")
    plt.close(fig)
    return path


def generate_all_diagrams(source: str | Path = "data/jtbd_scores.csv", output_dir: str | Path = "Diagrams") -> list[Path]:
    frame = pd.read_csv(source).sort_values(["opportunity", "jtbd"], ascending=[False, True]).reset_index(drop=True)
    out = Path(output_dir)
    out.mkdir(parents=True, exist_ok=True)
    outputs: list[Path] = []

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(frame["jtbd"], frame["opportunity"])
    ax.set_title("JTBD prioritization by opportunity score")
    ax.set_ylabel("Opportunity score")
    ax.tick_params(axis="x", rotation=15)
    outputs.append(_save(fig, out / "jtbd-prioritization.png"))

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(frame["importance"], frame["satisfaction"], s=90)
    for row in frame.itertuples():
        ax.annotate(row.jtbd, (row.importance, row.satisfaction), xytext=(6, 6), textcoords="offset points")
    ax.set_title("Importance vs satisfaction")
    ax.set_xlabel("Importance (1–10)")
    ax.set_ylabel("Satisfaction (1–10)")
    ax.set_xlim(0, 10.5)
    ax.set_ylim(0, 10.5)
    outputs.append(_save(fig, out / "importance-vs-satisfaction.png"))

    underserved = frame.assign(
        underserved_gap=(frame["importance"] - frame["satisfaction"]).clip(lower=0)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(underserved["jtbd"], underserved["underserved_gap"])
    ax.set_title("Underserved jobs: importance–satisfaction gap")
    ax.set_ylabel("Gap")
    ax.tick_params(axis="x", rotation=15)
    outputs.append(_save(fig, out / "underserved-jobs.png"))

    overserved = frame.assign(
        overserved_gap=(frame["satisfaction"] - frame["importance"]).clip(lower=0)
    )
    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(overserved["jtbd"], overserved["overserved_gap"])
    ax.set_title("Overserved jobs: satisfaction above importance")
    ax.set_ylabel("Overservice gap")
    ax.tick_params(axis="x", rotation=15)
    outputs.append(_save(fig, out / "overserved-jobs.png"))

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.scatter(frame["importance"], frame["opportunity"], s=90)
    for row in frame.itertuples():
        ax.annotate(row.jtbd, (row.importance, row.opportunity), xytext=(6, 6), textcoords="offset points")
    ax.set_title("Opportunity map")
    ax.set_xlabel("Job importance")
    ax.set_ylabel("Opportunity score")
    outputs.append(_save(fig, out / "opportunity-map.png"))

    fig, ax = plt.subplots(figsize=(9, 5))
    ax.bar(frame["jtbd"], frame["solution_job_fit"])
    ax.axhline(1.0, linestyle="--", linewidth=1)
    ax.set_title("Solution / job balance")
    ax.set_ylabel("Satisfaction / importance")
    ax.tick_params(axis="x", rotation=15)
    outputs.append(_save(fig, out / "solution-job-fit.png"))

    return outputs


def main() -> None:
    outputs = generate_all_diagrams()
    for path in outputs:
        print(path)


if __name__ == "__main__":
    main()
