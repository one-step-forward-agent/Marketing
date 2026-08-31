from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def test_validator_works_outside_repository_cwd(tmp_path: Path) -> None:
    repo_root = Path(__file__).resolve().parents[1]
    result = subprocess.run(
        [sys.executable, str(repo_root / "validate_interviews.py")],
        cwd=tmp_path,
        text=True,
        capture_output=True,
        check=False,
    )
    assert result.returncode == 0, result.stderr
    assert "Validated 30 synthetic CustDev fixtures" in result.stdout
