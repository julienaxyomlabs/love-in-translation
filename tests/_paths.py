"""Make ``src/`` and ``tools/`` importable when tests run without an installed package."""

import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
for folder in (ROOT / "src", ROOT / "tools"):
    if str(folder) not in sys.path:
        sys.path.insert(0, str(folder))
