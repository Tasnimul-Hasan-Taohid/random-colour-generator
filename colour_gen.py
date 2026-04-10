import random
import argparse
import colorsys
import os

def random_colour(seed=None):
    if seed is not None:
        random.seed(seed)
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def to_hex(r, g, b):
    return f"#{r:02X}{g:02X}{b:02X}"

def to_rgb(r, g, b):
    return f"rgb({r}, {g}, {b})"

def to_hsl(r, g, b):
    h, l, s = colorsys.rgb_to_hls(r / 255, g / 255, b / 255)
    return f"hsl({round(h * 360)}, {round(s * 100)}%, {round(l * 100)}%)"

def ansi_block(r, g, b):
    return f"\033[48;2;{r};{g};{b}m     \033[0m"

def print_colour(r, g, b):
    print(f"{ansi_block(r, g, b)}  Hex: {to_hex(r, g, b)}")
    print(f"         RGB: {to_rgb(r, g, b)}")
    print(f"         HSL: {to_hsl(r, g, b)}")
    print()

def main():
    parser = argparse.ArgumentParser(description="Random Colour Generator")
    parser.add_argument("--count", type=int, default=1, help="Number of colours to generate")
    parser.add_argument("--seed", type=int, default=None, help="Seed for reproducible output")
    parser.add_argument("--export", action="store_true", help="Export palette to palette.txt")
    args = parser.parse_args()

    colours = []
    for i in range(args.count):
        seed = args.seed + i if args.seed is not None else None
        r, g, b = random_colour(seed)
        colours.append((r, g, b))
        print_colour(r, g, b)

    if args.export:
        with open("palette.txt", "w") as f:
            for r, g, b in colours:
                f.write(f"{to_hex(r, g, b)} | {to_rgb(r, g, b)} | {to_hsl(r, g, b)}\n")
        print(f"Palette saved to palette.txt ({len(colours)} colour{'s' if len(colours) > 1 else ''})")

if __name__ == "__main__":
    main()
