"""
Challenge 8: Keyboard Art (Advanced Challenge)
Use keyboard keys to control drawing and create art.
Your turtle friend is named kheya!

Concepts used: Variables, conditionals, event handling (advanced!)
NOTE: This challenge uses concepts you'll learn more about later!
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Challenge 8: Keyboard Art")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(5)
kheya.color("white")

# Customization variables
move_distance = 20
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink", "cyan", "white"]
current_color_index = 0

# These are special functions that get called when keys are pressed
def move_up():
    kheya.setheading(90)  # Point up
    kheya.forward(move_distance)

def move_down():
    kheya.setheading(270)  # Point down
    kheya.forward(move_distance)

def move_left():
    kheya.setheading(180)  # Point left
    kheya.forward(move_distance)

def move_right():
    kheya.setheading(0)   # Point right
    kheya.forward(move_distance)

def change_color():
    global current_color_index
    current_color_index = (current_color_index + 1) % len(colors)
    kheya.color(colors[current_color_index])

def pen_up():
    kheya.penup()  # Stop drawing

def pen_down():
    kheya.pendown()  # Start drawing

def clear_screen():
    kheya.clear()  # Clear all drawings

# Your code here - add more special functions for other keys!
# Ideas: 
def draw_circle():
    # Your code: make kheya draw a small circle
    pass

def draw_square():
    for i in range(4):
        kheya.forward(50)
        kheya.right(90)

def go_to_center():
    # Your code: move kheya to the center (0, 0) without drawing
    pass

def stamp_turtle():
    # Your code: stamp the turtle shape at current position
    # Hint: Use kheya.stamp()
    pass

# Set up keyboard controls (this part is advanced - focus on the functions above!)
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")
screen.onkey(change_color, "space")
screen.onkey(pen_up, "u")
screen.onkey(pen_down, "d")
screen.onkey(clear_screen, "c")

# Add your new controls here!
# Example: screen.onkey(draw_circle, "o")  # Press 'o' to draw circle
screen.onkey(draw_square, "o")  # This will draw a square when 'o' is pressed

screen.listen()
print("Keyboard Controls:")
print("Arrow keys: Move kheya")
print("Spacebar: Change color")
print("U: Pen up")
print("D: Pen down") 
print("C: Clear screen")
print("")
print("Add more controls by completing the functions above!")
print("Then connect them to keys at the bottom of the code!")

# Keep the window open and listening for key presses
screen.mainloop()