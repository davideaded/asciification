#!/usr/bin/python3
from PIL import Image, ImageEnhance
import math, sys, shutil

ACCEPTABLE_FORMATS = ("jpeg", "jpg", "webp")

if len(sys.argv) < 2:
    print(f"[ERROR] {len(sys.argv)} arguments passed. Usage: {sys.argv[0]} <file>")
    sys.exit(1)

format = sys.argv[1].split(".")[-1].lower()
if not format in ACCEPTABLE_FORMATS:
    print(f"[ERRO] Format {format} still not supported")
    sys.exit(1)

def debug_img(img):
    print(f"DEBUGGING {img.filename}")
    print(f"IMG MODE:{img.mode}")
    print(f"IMG FORMAT:{img.format}")

def resize_img(img, max_width):
    aspect_ratio = img.height / img.width
    new_width = min(img.width, max_width)
    new_height = int(aspect_ratio * new_width * 0.55)
    return img.resize((new_width, new_height))


def get_grayscale_from_img(filename, max_width):
    try:
        with Image.open(filename) as im:
            debug_img(im)
            im = resize_img(im, max_width)
            im = im.convert("L")

            pixels = list(im.getdata())
            width, height = im.size

            return pixels, width, height

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
    except Exception as e:
        print(f"[ERROR] loading the image: {e}")

def print_ascii(filename, max_width=100):
    res = get_grayscale_from_img(filename, max_width)
    if res == None:
        return
    gs, w, h = res 
    shades = "@%#*+=-:. "

    ascii_art = []
    for y in range(h):
        line = ""
        for x in range(w):
            px_value = gs[y * w + x]
            line += shades[px_value * len(shades) // 256]
        ascii_art.append(line + "\n")

    for line in ascii_art:
        print(line)

filename = sys.argv[1]
terminal_width = shutil.get_terminal_size()[0]
print_ascii(filename, terminal_width // 2)
