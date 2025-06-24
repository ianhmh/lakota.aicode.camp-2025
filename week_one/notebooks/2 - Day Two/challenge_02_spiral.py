"""
Challenge 2: Draw a Spiral
Create a spiral that grows outward using loops and variables.
Your turtle friend is named kheya!

Concepts used: Variables, loops, growing patterns
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Challenge 2: Draw a Spiral")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(6)
kheya.color("green")

# Spiral customization variables - change these to modify your spiral!
turns = 50              # How many turns the spiral makes
start_size = 5          # Starting distance for each line
spiral_color = "green"  # Color of the spiral

# Set up the spiral
kheya.color(spiral_color)
size = start_size

# Draw the spiral
# Your code here - create a loop that draws the spiral
# Hints:
# - Use a for loop that runs 'turns' times
# - Each time through the loop:
#   * Move forward by 'size' 
#   * Turn left by some angle (try 91 degrees for a good spiral!)
#   * Increase 'size' by 'growth'

for i in range(turns):
    # Move forward
    kheya.forward(size)
    
    # Turn left (fill in the angle - try different values!)
    kheya.left(_)  # Fill in: what angle creates a good spiral?
    
    # Make the next line bigger
    size += _       # Fill in: how should the size grow each time?

# Keep the window open
screen.exitonclick()
print("Click the screen to close!")