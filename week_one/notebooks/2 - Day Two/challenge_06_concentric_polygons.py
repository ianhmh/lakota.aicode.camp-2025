"""
Challenge 6: Concentric Polygons
Draw multiple polygons inside each other, each with different colors.
Your turtle friend is named kheya!

Concepts used: Variables, nested loops, positioning
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("navy")
screen.setup(800, 600)
screen.title("Challenge 6: Concentric Polygons")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(6)

# Polygon customization variables
polygon_sides = 6       # Number of sides for each polygon (hexagon)
layers = 5              # How many polygons to draw
start_size = 100        # Size of the largest (outer) polygon
size_decrease = 15      # How much smaller each inner polygon is

# Colors for each layer
colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]

# Calculate the angle for turning (same for all polygons)
turn_angle = 360 / polygon_sides

# Draw the polygons from largest to smallest
current_size = start_size

for layer in range(layers):
    # Choose color for this layer
    color_index = layer % len(colors)
    kheya.color(colors[color_index])
    
    # Move to starting position for this polygon
    # We need to move inward as polygons get smaller
    start_x = -(current_size / 2)
    start_y = -(current_size / 2)
    
    kheya.penup()
    kheya.goto(start_x, start_y)
    kheya.pendown()
    kheya.setheading(0)  # Face right
    
    # Draw one polygon
    # Your code here - draw a polygon with 'polygon_sides' sides
    # Each side should be 'current_size' long
    # Use turn_angle to turn between sides
    
    for side in range(polygon_sides):
        # Draw one side and turn
        # Your code here:
        
        
    # Make the next polygon smaller
    current_size -= size_decrease

# Keep the window open
screen.exitonclick()
print("Click the screen to close!")