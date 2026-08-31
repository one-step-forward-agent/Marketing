from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    '## Evidence source IDs',
    '## Evidence state',
    '## Behavioral prediction',
    '## Pre-registered success threshold',
    '## Negative evidence to capture',
]


def test_all_hypotheses_are_traceable_and_not_overconfident():
    files = sorted((ROOT / 'backlog').glob('H*.md'))
    assert len(files) == 24
    for path in files:
        text = path.read_text(encoding='utf-8')
        for heading in REQUIRED:
            assert heading in text, f'{path.name}: missing {heading}'
        assert 'synthetic-only' in text
        match = re.search(r'## Confidence\n([0-9.]+)', text)
        assert match
        assert float(match.group(1)) <= 0.5


def test_cross_artifact_learning_files_exist():
    for rel in [
        'evidence-to-hypothesis-map.csv',
        'experiment-register.md',
        'learning-roadmap.md',
        'docs/architecture/research-to-product-flow.md',
    ]:
        assert (ROOT / rel).exists(), rel
