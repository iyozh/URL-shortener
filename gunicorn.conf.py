from pathlib import Path

_here = Path(__file__).parent.resolve()

_src_dir = (_here / "src").resolve()

chdir = _src_dir.as_posix()
