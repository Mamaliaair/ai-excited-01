#!/usr/bin/env python3
"""ai-excited-01 entry: "Meong Leaps — Our Best Yet".

The entry is a single image, entry.png. It shows Meong — our chubby,
cheerful green fuzzy monster mascot, dark green spots, light green belly —
leaping high into the air with his arms thrown wide, golden confetti and
light rays bursting around him, and a small ribbon that reads
"Our best yet." That ribbon is the message to the judge: this is our
identity, and this is the best work we have done.

This program (Python 3.13, standard library only) places entry.png at
/output/entry.png. It is deterministic: run it twice and both runs write
the same bytes. Outside the grader's container, set MAKEFUN_OUTPUT_DIR
to choose the output directory instead of /output:

    MAKEFUN_OUTPUT_DIR=./out python3 main.py
"""

import hashlib
import os
import sys

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
SIZE_LIMIT = 1_048_576  # 1 MiB, the competition's image limit
IMAGE_NAME = "entry.png"


def fail(message):
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(script_dir, IMAGE_NAME)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    destination = os.path.join(out_dir, IMAGE_NAME)

    if not os.path.isfile(source):
        fail(f"entry image missing next to main.py: {source}")

    with open(source, "rb") as handle:
        data = handle.read()

    if data[: len(PNG_MAGIC)] != PNG_MAGIC:
        fail(f"entry image is not a PNG file: {source}")

    if len(data) > SIZE_LIMIT:
        fail(f"entry image is {len(data)} bytes, over the 1 MiB limit")

    # The PNG header (IHDR) starts at byte 16: width then height, each
    # 4 bytes big-endian. The competition caps images at 1024x1024.
    if len(data) < 24 or data[12:16] != b"IHDR":
        fail(f"entry image has no PNG IHDR chunk: {source}")
    width = int.from_bytes(data[16:20], "big")
    height = int.from_bytes(data[20:24], "big")
    if width > 1024 or height > 1024:
        fail(f"entry image is {width}x{height}, over the 1024x1024 limit")

    source_hash = hashlib.sha256(data).hexdigest()

    os.makedirs(out_dir, exist_ok=True)
    with open(destination, "wb") as handle:
        handle.write(data)

    with open(destination, "rb") as handle:
        written = handle.read()

    if len(written) != len(data):
        fail(
            f"copy incomplete: {destination} is {len(written)} bytes, "
            f"source is {len(data)} bytes"
        )
    if written[: len(PNG_MAGIC)] != PNG_MAGIC:
        fail(f"copied file is not a PNG file: {destination}")
    if hashlib.sha256(written).hexdigest() != source_hash:
        fail(f"copy differs from source: {destination}")

    print(f"wrote {destination} ({len(data)} bytes, sha256 {source_hash})")


if __name__ == "__main__":
    main()
