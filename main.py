#!/usr/bin/python3
from PIL import Image, ImageEnhance
import math, sys, shutil

ACCEPTABLE_FORMATS = ("jpeg", "jpg", "webp")
FLAGS = (
        {
            "short": "-h",
            "full": "--help",
            "description": "Display this help",
        },
        {
            "short": "-d",
            "full": "--dd",
            "description": "Testano bagui doido kkkkkkkkkk",

        }
    )


if len(sys.argv) < 2:
    print(f"[ERROR] {len(sys.argv)} arguments passed. Usage: {sys.argv[0]} [OPTION] FILE")
    sys.exit(1)

flags = []
filename = None
for arg in sys.argv[1:]:
    if arg.startswith("-"):
        flags.append(arg)
    else:
        filename = arg
print("[DEBUG] ", flags, filename)

if filename and not filename.split(".")[-1] in ACCEPTABLE_FORMATS:
    print(f"[ERRO] Format {format} still not supported")
    sys.exit(1)

def help():
    print(f"Usage: {sys.argv[0]} [OPTION] FILE\n")
    for flag in FLAGS:
        print(f"{flag['short']}, {flag['full']}\t{flag['description']}")

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

terminal_width = shutil.get_terminal_size()[0]
print_ascii(filename, terminal_width // 2)
