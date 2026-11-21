"""Entry point for the news-image-20261120 competition entry.

The poster itself lives in this repository as entry.png (drawn by
build_poster.py). This program's whole job is to deliver that image:
it copies entry.png, byte for byte, to entry.png inside the output
directory — /output by default, or the folder named by the
MAKEFUN_OUTPUT_DIR environment variable when that is set. Because it
only copies a fixed file, running it twice writes identical bytes.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def deliver():
    if not SOURCE.exists():
        raise SystemExit(f"entry image missing: {SOURCE}")
    target_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "entry.png"
    shutil.copyfile(SOURCE, target)
    return target


if __name__ == "__main__":
    written = deliver()
    print(f"wrote {written} ({written.stat().st_size} bytes)")
