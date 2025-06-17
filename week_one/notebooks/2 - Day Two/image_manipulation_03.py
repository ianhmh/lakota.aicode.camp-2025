"""
Detects edges with OpenCV’s Canny and sketches them as continuous strokes.
Dependencies : opencv-python, numpy
Run          : python edge_sketch.py
"""

# conda install -c conda-forge opencv

import cv2
import numpy as np
import turtle

# ---------- SETTINGS ----------
IMAGE_FILE = "week_one/notebooks/2 - Day Two/190253-1.jpg"
BLUR_KSIZE = 3        # Gaussian blur kernel size
CANNY_LOW  = 50       # Canny thresholds
CANNY_HIGH = 150
STEP       = 1        # sample every Nth pixel horizontally
# ------------------------------

# Edge detection
img   = cv2.imread(IMAGE_FILE)
gray  = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur  = cv2.GaussianBlur(gray, (BLUR_KSIZE, BLUR_KSIZE), 0)
edges = cv2.Canny(blur, CANNY_LOW, CANNY_HIGH)

h, w = edges.shape

# Turtle setup
turtle.colormode(255)
scr = turtle.Screen()
scr.setup(w, h)
scr.bgcolor("white")
scr.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.color("black")
pen.speed(0)
pen.penup()

offset_x, offset_y = -w / 2, h / 2

# Draw continuous horizontal strokes
for y in range(h):
    drawing = False
    for x in range(0, w, STEP):
        if edges[y, x]:          # edge pixel
            if not drawing:
                pen.penup()
                pen.goto(x + offset_x, offset_y - y)
                pen.pendown()
                drawing = True
        else:
            if drawing:
                drawing = False

scr.update()
turtle.done()
