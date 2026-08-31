from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent
REQUIRED = [
    "## Related JTBD",
    "## Problem statement",
    "## Evidence",
    "## Evidence source IDs",
    "## Evidence state",
    "## Assumption",
    "## Behavioral prediction",
    "## Proposed experiment",
    "## Pre-registered success threshold",
    "## Expected impact",
    "## Implementation complexity",
    "## Confidence",
    "## Priority score",
    "## Negative evidence to capture",
    "## Success metric",
    "## Kill criterion",
    "## Dependencies",
    "## Status",
]

def parse_priority(text: str) -> float:
    match = re.search(r"## Priority score\n([0-9.]+)", text)
    if not match:
        raise ValueError("priority missing")
    return float(match.group(1))

def parse_confidence(text: str) -> float:
    match = re.search(r"## Confidence\n([0-9.]+)", text)
    if not match:
        raise ValueError("confidence missing")
    return float(match.group(1))

def main() -> int:
    files = sorted((ROOT / "backlog").glob("H*.md"))
    expected = [f"H{i:03d}.md" for i in range(1, 25)]
    if [p.name for p in files] != expected:
        print(f"Expected exactly H001.md..H024.md, got {[p.name for p in files]}", file=sys.stderr)
        return 1
    priorities = {}
    for path in files:
        text = path.read_text(encoding="utf-8")
        missing = [field for field in REQUIRED if field not in text]
        if missing:
            print(f"{path}: missing {missing}", file=sys.stderr)
            return 1
        if "synthetic-only" not in text:
            print(f"{path}: evidence state must be explicit", file=sys.stderr)
            return 1
        if parse_confidence(text) > 0.5:
            print(f"{path}: synthetic-stage confidence cannot exceed 0.5", file=sys.stderr)
            return 1
        priorities[path.stem] = parse_priority(text)
    backlog = ROOT / "product-backlog.md"
    if not backlog.exists():
        print("product-backlog.md missing", file=sys.stderr)
        return 1
    order = re.findall(r"\| (H\d{3}) \|", backlog.read_text(encoding="utf-8"))
    if len(order) != 24 or set(order) != set(priorities):
        print("Backlog does not list all 24 hypotheses exactly once", file=sys.stderr)
        return 1
    expected_order = sorted(priorities, key=lambda hid: (-priorities[hid], hid))
    if order != expected_order:
        print("Backlog is not sorted by priority descending, ID ascending", file=sys.stderr)
        return 1
    print("Validated 24 traceable ranked hypotheses")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
