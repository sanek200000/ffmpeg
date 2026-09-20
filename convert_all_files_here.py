import subprocess
from pathlib import Path

CURRENT_DIR = Path(__file__).resolve().parent
SUFFIX = "*.mkv"
PREFIX = "out_"
OUT_SUFFIX = ".mkv"


def get_command(filepath: Path, out_filepath: Path) -> str:
    return f"""ffmpeg -i \
            '{filepath}' \
            -map 0:v:0 \
            -map 0:a:6 \
            -map 0:s \
            -map_metadata -1 -map_chapters -1 \
            -filter:v "setpts=PTS/1.25" \
            -filter:a "atempo=1.25" \
            -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
            -c:a ac3 -b:a 192k \
            '{out_filepath}'
        """


if __name__ == "__main__":
    for filepath in CURRENT_DIR.glob(SUFFIX):
        stem = filepath.stem
        out_filepath = filepath.parent.joinpath(PREFIX + stem + OUT_SUFFIX)

        if out_filepath.exists():
            continue

        command = get_command(filepath, out_filepath)
        subprocess.run(command, shell=True, check=True)
