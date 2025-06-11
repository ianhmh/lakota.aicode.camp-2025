"""
Challenge 9: Pattern Drawing (Advanced Challenge)
Draw a pattern for others to copy, then let them try to recreate it.
Your turtle friend is named kheya!

Concepts used: Variables, loops, conditionals, positioning
NOTE: This challenge combines many concepts and uses some advanced features!
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("white")
screen.setup(800, 600)
screen.title("Challenge 9: Pattern Drawing")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(5)

# Pattern customization variables
pattern_color = "gray"
drawing_color = "blue"
pattern_size = 50

print("Welcome to the Pattern Drawing Challenge!")
print("First, you'll create a pattern. Then someone else can try to copy it!")

# Part 1: Create the target pattern
kheya.color(pattern_color)
kheya.penup()
kheya.goto(-150, 0)  # Start on the left side
kheya.pendown()

print("Creating a pattern for others to copy...")

# Your code here - create an interesting but copyable pattern
# Ideas: 
# - Draw a simple house (square + triangle)
# - Draw a flower (circle + petals)
# - Draw your initials
# - Draw simple geometric shapes
# Keep it simple so someone can copy it!

# Example pattern (you can replace this):
# Simple house
kheya.forward(pattern_size)  # bottom of house
kheya.left(90)
kheya.forward(pattern_size)  # left side
kheya.left(90)
kheya.forward(pattern_size)  # top of house
kheya.left(90)
kheya.forward(pattern_size)  # right side
# # Add a triangle roof
kheya.left(90)
kheya.left(45)
kheya.forward(pattern_size * 0.7)  # roof side 1
kheya.left(90)
kheya.forward(pattern_size * 0.7)  # roof side 2

# Your pattern code here:


# Part 2: Set up for copying
print("\nPattern complete!")
input("Study the gray pattern carefully, then press Enter to start copying it!")

# Move to the right side for drawing the copy
kheya.penup()
kheya.goto(50, 0)  # Right side of screen
kheya.pendown()
kheya.color(drawing_color)

print("\nNow try to recreate the pattern in blue!")
print("Drawing controls:")
print("- Use the arrow keys to move kheya")
print("- Press 'u' to lift the pen (move without drawing)")
print("- Press 'd' to put the pen down (start drawing)")
print("- Press 'c' to clear your drawing and start over")

# Movement functions for copying (advanced - focus on the pattern above!)
def move_up():
    kheya.setheading(90)
    kheya.forward(20)

def move_down():
    kheya.setheading(270)
    kheya.forward(20)

def move_left():
    kheya.setheading(180)
    kheya.forward(20)

def move_right():
    kheya.setheading(0)
    kheya.forward(20)

def pen_up():
    kheya.penup()

def pen_down():
    kheya.pendown()

def clear_drawing():
    # Clear only the blue drawing, keep the gray pattern
    current_pos = kheya.position()
    kheya.penup()
    kheya.goto(50, -200)
    kheya.pendown()
    kheya.color("white")
    kheya.begin_fill()
    for _ in range(4):
        kheya.forward(300)
        kheya.left(90)
    kheya.end_fill()
    kheya.color(drawing_color)
    kheya.goto(current_pos)

# Set up keyboard controls
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(clear_drawing, "c")
screen.listen()

# Keep the window open
screen.mainloop()