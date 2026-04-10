# random-colour-generator

![build passing](https://img.shields.io/badge/build-passing-brightgreen) ![python 3.8+](https://img.shields.io/badge/python-3.8+-blue) ![MIT license](https://img.shields.io/badge/license-MIT-orange)

A zero-dependency Python tool that generates random colours in `hex`, `RGB`, and `HSL` formats. Run it once for a single colour, or generate an entire palette and export it — all from the terminal.

## Features

- Generates colours in hex, RGB, and HSL simultaneously
- Coloured terminal preview using ANSI escape codes
- Optional seed for reproducible palettes
- Batch mode — generate N colours at once
- Export palette to `palette.txt`
- Zero dependencies — pure Python stdlib

## Quick start

```bash
git clone https://github.com/tasnimul-hasan/random-colour-generator
cd random-colour-generator
python colour_gen.py
```

## Usage

```bash
# single random colour
python colour_gen.py

# generate 5 colours
python colour_gen.py --count 5

# reproducible palette with a seed
python colour_gen.py --count 8 --seed 42

# export to file
python colour_gen.py --count 10 --export
```

## Example output

```
█████  Hex:  #A34FB7
       RGB:  rgb(163, 79, 183)
       HSL:  hsl(288, 40%, 51%)
```

## Project structure

```
random-colour-generator/
├── src/
│   ├── __init__.py
│   └── colour.py       # core logic as importable module
├── colour_gen.py        # CLI entry point
├── requirements.txt
├── LICENSE
└── README.md
```

## Use as a module

```python
from src.colour import random_colour, to_hex, to_rgb, to_hsl

r, g, b = random_colour(seed=99)
print(to_hex(r, g, b))   # #4A9FD2
print(to_rgb(r, g, b))   # rgb(74, 159, 210)
print(to_hsl(r, g, b))   # hsl(204, 57%, 56%)
```

## License

MIT © [Tasnimul Hasan](https://linkedin.com/in/tasnimul-hasan-taohid)
