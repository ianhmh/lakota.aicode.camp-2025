"""
Challenge 5: Rainbow Spiral
Create a spiral where each segment is a different color.
Your turtle friend is named kheya!

Concepts used: Variables, loops, lists, modulo operator
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Challenge 5: Rainbow Spiral")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(6)

# Rainbow spiral customization variables
segments = 50           # Number of segments in the spiral
start_length = 5        # Starting length of each line
growth = 2              # How much each line grows
turn_angle = 91         # Angle to turn (try different values!)

# Rainbow colors - kheya will cycle through these
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

# Start drawing the rainbow spiral
current_length = start_length

for i in range(segments):
    # Choose the color for this segment
    # The modulo operator (%) cycles through the color list
    color_index = i % len(colors)
    kheya.color(colors[color_index])
    
    # Your code here!
    # Draw one segment of the spiral:
    # 1. Move forward by current_length
    # 2. Turn left by turn_angle
    # 3. Increase current_length by growth
    
    # Hint: This is very similar to Challenge 2, but with changing colors!
    
    
    # Make the next segment a little longer
    current_length += growth

# Keep the window open
screen.exitonclick()
print("Click the screen to close!")