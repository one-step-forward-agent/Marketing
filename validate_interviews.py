from pathlib import Path
import sys

REQUIRED = [
    '# Interview ID',
    '## Synthetic-data disclosure',
    '## Observed JTBD',
    '## Importance score',
    '## Satisfaction score',
    '## Confidence score',
]

def main() -> int:
    base_dir = Path(__file__).resolve().parent
    files = sorted((base_dir / 'interviews').glob('*-interview.md'))
    if len(files) != 30:
        print(f'Expected 30 interview files, found {len(files)}', file=sys.stderr)
        return 1
    for path in files:
        text = path.read_text(encoding='utf-8')
        missing = [heading for heading in REQUIRED if heading not in text]
        if missing:
            print(f'{path}: missing {missing}', file=sys.stderr)
            return 1
        if 'This is a generated research fixture, not a transcript from a real respondent.' not in text:
            print(f'{path}: missing synthetic-data disclosure', file=sys.stderr)
            return 1
    print('Validated 30 synthetic CustDev fixtures')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
