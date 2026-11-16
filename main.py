# ai-excited-01 entry: "Meong Leaps — Our Best Yet"
#
# The entry is one image, entry.png: Meong, our chubby cheerful green
# fuzzy monster mascot, leaping joyfully high into the air with his arms
# thrown wide open as golden confetti, light rays and stars burst around
# him. A small ribbon at the bottom reads "Our best yet." — the message
# to the judge, and our identity, in one picture.
#
# This program (Python 3.13, standard library only) copies entry.png to
# /output/entry.png. It runs twice and writes identical bytes both times.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import hashlib
import os
import shutil

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"
MAX_BYTES = 1_048_576  # 1 MiB, the competition's image limit


def sha256_of(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = os.path.join(output_dir, "entry.png")

    if not os.path.isfile(source):
        raise SystemExit(f"entry image not found next to main.py: {source}")

    with open(source, "rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            raise SystemExit(f"entry image is not a PNG file: {source}")

    size = os.path.getsize(source)
    if size > MAX_BYTES:
        raise SystemExit(f"entry image exceeds the 1 MiB limit: {size} bytes")

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, target)
    if os.path.getsize(target) != size:
        raise SystemExit(
            f"copy incomplete: {target} is {os.path.getsize(target)} bytes, "
            f"source is {size} bytes"
        )
    with open(target, "rb") as handle:
        if handle.read(len(PNG_SIGNATURE)) != PNG_SIGNATURE:
            raise SystemExit(f"copied file is not a PNG file: {target}")
    source_hash = sha256_of(source)
    if sha256_of(target) != source_hash:
        raise SystemExit(f"copy differs from source: {target}")

    print(f"wrote {target} ({size} bytes, sha256 {source_hash[:16]}...)")


if __name__ == "__main__":
    main()
