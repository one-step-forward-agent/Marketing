from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_SECTIONS = [
    '## Functional job',
    '## Emotional job',
    '## Social job',
    '## Switching forces',
    '## Alternative considered',
    '## Evidence type',
    '## Interpretation risk',
]


def test_all_interviews_have_research_quality_sections():
    files = sorted((ROOT / 'interviews').glob('*-interview.md'))
    assert len(files) == 30
    for path in files:
        text = path.read_text(encoding='utf-8')
        for heading in REQUIRED_SECTIONS:
            assert heading in text, f'{path.name}: missing {heading}'
        assert 'Synthetic fixture' in text


def test_research_synthesis_artifacts_exist():
    required = [
        ROOT / 'analysis' / 'evidence-matrix.csv',
        ROOT / 'analysis' / 'segment-analysis.md',
        ROOT / 'analysis' / 'research-quality.md',
        ROOT / 'analysis' / 'research-gaps.md',
        ROOT / 'analysis' / 'next-interview-guide.md',
    ]
    assert all(path.exists() for path in required)
