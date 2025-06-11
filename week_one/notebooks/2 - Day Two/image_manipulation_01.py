"""
Draws a low-resolution pointillist version of an image.
Dependencies : Pillow
Run          : python dot_painter.py
"""

from PIL import Image
import turtle

# ---------- SETTINGS ----------
IMAGE_FILE  = "week_one/notebooks/2 - Day Two/190253-1.jpg"
SCALE       = 4      # 1 = full resolution, 2 = half, … 8 = ⅛th
DOT_SIZE    = 0.5       # diameter in pixels
# ------------------------------

# Load & down-sample
img = Image.open(IMAGE_FILE).convert("RGB")
w, h = img.size
w //= SCALE
h //= SCALE
img = img.resize((w, h), Image.NEAREST)

# Turtle setup
turtle.colormode(255)
scr = turtle.Screen()
scr.setup(w, h)
scr.tracer(0, 0)          # turn off incremental drawing
pen = turtle.Turtle()
pen.hideturtle()
pen.penup()

# Coordinate helper (image origin top-left ➜ turtle origin centre)
offset_x, offset_y = -w / 2, h / 2

for y in range(h):
    for x in range(w):
        pen.goto(x + offset_x, offset_y - y)
        pen.dot(DOT_SIZE, img.getpixel((x, y)))

scr.update()
turtle.done()
