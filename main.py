from PIL import Image, ImageFilter
import math

ACCEPTABLE_FORMATS = ("JPEG", "JPG", "WEBP")

def debug_img(img):
    print(f"DEBUGGING {img.filename}")
    print(f"IMG MODE:{img.mode}")
    print(f"IMG FORMAT:{img.format}")

def resize_img(img, max_width):
    aspect_ratio = img.height / img.width
    new_width = min(img.width, max_width)
    new_height = int(aspect_ratio * new_width * 0.50)
    return img.resize((new_width, new_height))

def get_grayscale_from_img(filename, max_width):
    try:
        with Image.open(filename) as im:
            debug_img(im)
            if im.format not in(ACCEPTABLE_FORMATS):
                print(f"[WARN] Format {im.format} still not supported")
                return None

            im = resize_img(im, max_width)

            pixels = im.load()
            width, height = im.size
            gray_scaled_pixels = []
            for y in range(height):
                for x in range(width):
                    cpixel = pixels[x, y]
                    lum = math.floor((0.3 * cpixel[0]) + (0.59 * cpixel[1]) + (0.11 * cpixel[2]))
                    gray_scaled_pixels.append(lum)

            return gray_scaled_pixels, width, height

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
    except Exception as e:
        print(f"[ERROR] loading the image: {e}")


# mapping luminosity to only two chars: @ and .

def print_ascii(filename, max_width=100):
    res = get_grayscale_from_img(filename, max_width)
    if res == None:
        return
    gs, w, h = res 

    ascii_art = []
    for y in range(h):
        line = ""
        shades = "@#%. "
        for x in range(w):
            px_value = gs[y * w + x]
            line += shades[px_value * len(shades) // 256]
        ascii_art.append(line + "\n")

    print("Done")

    for line in ascii_art:
        print(line)

print_ascii("testimg/sp.jpg", 50)
