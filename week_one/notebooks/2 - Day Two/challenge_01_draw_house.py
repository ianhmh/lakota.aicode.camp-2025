"""
Challenge 1: Draw a House
Draw a house using variables to control size and colors.
Your turtle friend is named kheya!

Concepts used: Variables, loops, turtle positioning
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(800, 600)
screen.title("Challenge 1: Draw a House")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(5)

# House customization variables - change these to modify your house!
house_size = 100        # Size of the house walls
wall_color = "brown"    # Color of the walls
roof_color = "red"      # Color of the roof

# Position for the house
house_x = 0             # X position (left/right)
house_y = -50           # Y position (up/down)

# Move kheya to starting position
kheya.penup()
kheya.goto(house_x, house_y)
kheya.pendown()

# Draw the walls (square)
kheya.color(wall_color)
# Your code here - draw a square for the walls using house_size
# Hint: Use a for loop to draw 4 sides
# Each side should be 'house_size' long


# Draw the roof (triangle) 
# First, move to the top-left corner of the house
kheya.penup()
kheya.goto(house_x, house_y + house_size)
kheya.pendown()

kheya.color(roof_color)
# Your code here - draw a triangle for the roof
# Hint: A triangle has 3 sides with 120-degree turns


# Optional: Add a door and/or windows!
# Ideas:
# - Draw a rectangle for a door
# - Draw small squares for windows
# - Use different colors
# Your creative additions here:


# Keep the window open
screen.exitonclick()
print("Click the screen to close!")