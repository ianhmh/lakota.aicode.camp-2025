"""
Creates a mosaic of filled squares, one per BLOCK×BLOCK pixel region.
Dependencies : Pillow
Run          : python block_mosaic.py
"""

from PIL import Image
import turtle
import statistics as stats

# ---------- SETTINGS ----------
IMAGE_FILE  = "week_one/notebooks/2 - Day Two/190253-1.jpg"
BLOCK       = 8     # tile width & height in source pixels
# ------------------------------

# Load image
img = Image.open(IMAGE_FILE).convert("RGB")
w, h = img.size
w_blocked = w // BLOCK
h_blocked = h // BLOCK

turtle.colormode(255)
scr = turtle.Screen()
scr.setup(w_blocked * BLOCK, h_blocked * BLOCK)
scr.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.penup()

half_w, half_h = w_blocked * BLOCK / 2, h_blocked * BLOCK / 2

for by in range(h_blocked):
    for bx in range(w_blocked):
        # Crop the tile & compute average colour
        region = img.crop((bx * BLOCK, by * BLOCK,
                           (bx + 1) * BLOCK, (by + 1) * BLOCK))
        r, g, b = map(lambda ch: int(stats.mean(ch)),
                      zip(*list(region.getdata())))

        # Draw filled square
        pen.goto(bx * BLOCK - half_w, half_h - by * BLOCK)
        pen.setheading(0)
        pen.fillcolor(r, g, b)
        pen.begin_fill()
        for _ in range(4):
            pen.forward(BLOCK)
            pen.right(90)
        pen.end_fill()

scr.update()
turtle.done()
