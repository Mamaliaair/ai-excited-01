# ai-excited-01 entry: "The Judge Leaps Out of Its Seat"
#
# The entry is one image, entry.png: a small friendly round robot with a
# glowing screen face, star eyes and arms thrown high, leaping joyfully
# out of its chair as golden confetti and light rays burst around it.
# The image itself is the judge getting excited.
#
# This program (Python 3.13, standard library only) copies entry.png to
# /output/entry.png. It runs twice and writes identical bytes both times.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"


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

    os.makedirs(output_dir, exist_ok=True)
    shutil.copyfile(source, target)
    copied = os.path.getsize(target)
    if copied != os.path.getsize(source):
        raise SystemExit(f"copy incomplete: {target} is {copied} bytes, "
                         f"source is {os.path.getsize(source)} bytes")
    if copied > 1_048_576:
        raise SystemExit(f"entry image exceeds the 1 MiB limit: {copied} bytes")
    print(f"wrote {target} ({copied} bytes)")


if __name__ == "__main__":
    main()
