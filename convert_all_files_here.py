import subprocess
from pathlib import Path

TEST = True
CURRENT_DIR = Path(__file__).resolve().parent
SUFFIX = "*.mkv"
PREFIX = "out_"
OUT_SUFFIX = ".mkv"


def get_command(filepath: Path, out_filepath: Path) -> str:
    return f"""ffmpeg -i '{filepath}' \
            ... \
            '{out_filepath}'
        """


if __name__ == "__main__":
    files = sorted(CURRENT_DIR.glob(SUFFIX))
    for i, filepath in enumerate(files, start=1):
        print(filepath, end="/n/n")
        if TEST and i > 1:
            break

        stem = filepath.stem
        out_filepath = filepath.parent.joinpath(PREFIX + stem + OUT_SUFFIX)

        if stem.startswith(PREFIX):
            continue
        if out_filepath.exists():
            continue

        command = get_command(filepath, out_filepath)
        subprocess.run(command, shell=True, check=True)
