"""
Challenge 3: Draw a Flower
Create a flower with petals using loops and variables.
Your turtle friend is named kheya!

Concepts used: Variables, loops, lists
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("darkgreen")
screen.setup(800, 600)
screen.title("Challenge 3: Draw a Flower")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(5)

# Flower customization variables - change these to modify your flower!
petals = 8              # Number of petals
petal_size = 30         # Size of each petal
center_color = "yellow" # Color of the flower center
center_size = 20        # Size of the flower center

# Colors for the petals - kheya will cycle through these
petal_colors = ["red", "orange", "yellow", "pink", "purple", "magenta", "cyan"]

# Calculate how much to turn between each petal
angle_between_petals = 360 / petals

# Draw the petals
for i in range(petals):
    # Choose a color for this petal
    color_index = i % len(petal_colors)  # This cycles through the colors
    kheya.color(petal_colors[color_index])
    
    # Draw one petal here
    # Your code - draw a petal (could be a circle, oval, or custom shape)
    # Ideas:
    # - kheya.circle(petal_size) for a circular petal
    # - Draw a small triangle or oval shape
    # - Get creative with your petal design!
    
    
    # Turn to position for the next petal
    kheya.left(angle_between_petals)

# Draw the center of the flower
kheya.color(center_color)
# Your code here - draw the center of the flower
# Ideas:
# - kheya.circle(center_size) for a circular center
# - Use kheya.dot(center_size) for a solid dot
# - Draw a small shape in the center


# Keep the window open
screen.exitonclick()
print("Click the screen to close!")