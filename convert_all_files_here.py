from pathlib import Path
import subprocess

CURRENT_DIR = Path(__file__).resolve().parent
SUFFIX = "*.mkv"
PREFIX = "out_"
OUT_SUFFIX = ".mkv"


def get_command(filepath: Path) -> str:
    name = filepath.name
    stem = filepath.stem

    return f"""ffmpeg -i \
            {name} \
            -map 0:v:0 \
            -map 0:a:6 \
            -map 0:s \
            -map_metadata -1 -map_chapters -1 \
            -filter:v "setpts=PTS/1.25" \
            -filter:a "atempo=1.25" \
            -c:v libx264 -crf 18 -preset medium -pix_fmt yuv420p \
            -c:a ac3 -b:a 192k \
            {PREFIX}{stem}{OUT_SUFFIX}
        """


if __name__ == "__main__":
    for filepath in CURRENT_DIR.glob(SUFFIX):
        command = get_command(filepath)

        subprocess.run(command, shell=True, check=True)
