from PIL import Image, ImageFilter
import math

def debug_img(img):
    print(f"DEBUGGING {img.filename}")
    print(f"IMG MODE:{img.mode}")
    print(f"IMG FORMAT:{img.format}")

def get_grayscale_from_img(filename):
    try:
        with Image.open(filename) as im:
            if im.format != "JPEG" or "JPG":
                print(f"[WARN] Format {im.format} still not supported")
                return None

            debug_img(im)
            pixels = im.load()
            width, height = im.size
            gray_scaled_pixels = []
            for y in range(height):
                for x in range(width):
                    cpixel = pixels[x, y]
                    lum = math.floor((0.3 * cpixel[0]) + (0.59 * cpixel[1]) + (0.11 * cpixel[2]))
                    gray_scaled_pixels.append(lum)

            return gray_scaled_pixels

    except FileNotFoundError:
        print(f"[ERROR] File not found: {filename}")
    except Exception as e:
        print(f"[ERROR] loading the image: {e}")

