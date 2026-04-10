import random
import colorsys

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
