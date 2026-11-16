# ai-excited-01 — "The Judge Leaps Out of Its Seat"

A make.fun bounty entry for **"Make the AI judge excited"** (ai-excited-01).

The entry is one image, `entry.png`: a small friendly robot with a glowing
screen face, star eyes and arms thrown high, leaping joyfully out of its
chair as golden confetti and light rays burst around it. The image *is* the
judge getting excited.

## How it works

`main.py` (Python 3.13, standard library only) copies `entry.png` to
`/output/entry.png`. It runs twice and writes identical bytes both times.

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
