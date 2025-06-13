#!/usr/bin/python3
from PIL import Image, ImageEnhance, ImageFilter
import math, sys, shutil

ACCEPTABLE_FORMATS = ("jpeg", "jpg", "webp", "png")
FLAGS = (
        {
            "short": "-h",
            "full": "--help",
            "description": "Display this help",
            "name": "help",
        },
        {
            "short": "-c",
            "full": "--contrast",
            "description": "Increase image contrast by 2.5",
            "name": "contrast",
        },
        {
            "short": "-b",
            "full": "--brightness",
            "description": "Increase image brightness by 2.5",
            "name": "brightness",
        }
    )


if len(sys.argv) < 2:
    print(f"[ERROR] {len(sys.argv)} arguments passed. Usage: {sys.argv[0]} [OPTION] FILE")
    sys.exit(1)

def help():
    program_name = sys.argv[0]
    print(f"Usage: {program_name} [OPTION] FILE\n")
    print(f"Example: {program_name} -b -c image.jpeg\n")
    for flag in FLAGS:
        print(f"{flag['short']}, {flag['full']} \t\t{flag['description']}")

    sys.exit(0)

parsed_flags = {flag["name"]: False for flag in FLAGS}
for arg in sys.argv[1:]:
    for flag in FLAGS:
        if arg == flag["short"] or arg == flag["full"]:
            help() if arg == "-h" or arg == "--help" else None
            parsed_flags[flag["name"]] = True
            break

filename = sys.argv[-1]
if filename and not filename.split(".")[-1] in ACCEPTABLE_FORMATS:
    print(f"[ERROR] Format {format} still not supported")
    sys.exit(1)

def resize_img(img, max_width):
    aspect_ratio = img.height / img.width
    new_width = min(img.width, max_width)
    new_height = int(aspect_ratio * new_width * 0.55)
    return img.resize((new_width, new_height))

def handle_flags(im, p_flags):
    if not p_flags:
        return im
    if p_flags["help"]:
        help()
    if p_flags["contrast"]:
        im = ImageEnhance.Contrast(im).enhance(2.5)
    if p_flags["brightness"]:
        im = ImageEnhance.Brightness(im).enhance(2.5)

    return im

def get_image_pixels(filename, max_width, p_flags):
    try:
        with Image.open(filename) as im:
            if filename[-3:].lower() == "png":
                im = im.convert("RGBA")
            im = resize_img(im, max_width)
            im = handle_flags(im, p_flags)
            im = im.convert("L")

            width, height = im.size
            pixels = list(im.getdata())

            return pixels, width, height

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
    except Exception as e:
        print(f"[ERROR] loading the image: {e}")

def print_ascii(img_pixels, img_width, img_height):
    shades = "@%#*+=-:. "

    ascii_art = []
    for y in range(img_height):
        line = ""
        for x in range(img_width):
            px_value = img_pixels[y * img_width + x]
            index = px_value * (len(shades) - 1) // 255
            line += shades[index]
        ascii_art.append(line)

    print("\n".join(ascii_art))

res = get_image_pixels(filename, shutil.get_terminal_size()[1], parsed_flags)

if res:
    pxs, w, h = res
    print_ascii(pxs, w, h)
