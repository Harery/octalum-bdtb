import sys
from pathlib import Path

# Make src/ importable without installing.
ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "src"))
