# A make.fun ai-excited-01 entry (Python 3.13, standard library only).
# The image beside this file is the entry: "The Judge Leaps Out of Its
# Seat" — a small friendly robot with a glowing screen face, star eyes
# and arms thrown high, leaping joyfully out of its chair as golden
# confetti and light rays burst around it. The program copies it to
# /output/entry.png.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
import shutil

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
SOURCE = os.path.join(os.path.dirname(__file__), "entry.png")
TARGET = os.path.join(OUTPUT_DIR, "entry.png")

if not os.path.isfile(SOURCE):
    raise FileNotFoundError(f"entry image missing next to main.py: {SOURCE}")

os.makedirs(OUTPUT_DIR, exist_ok=True)
shutil.copyfile(SOURCE, TARGET)
print(f"wrote {TARGET} ({os.path.getsize(TARGET)} bytes)")
