"""
Challenge 7: Click-to-Draw (Advanced Challenge)
Create a program where clicking on the screen draws something at that location.
Your turtle friend is named kheya!

Concepts used: Variables, conditionals, event handling (advanced!)
NOTE: This challenge uses concepts you'll learn more about later!
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("lightgray")
screen.setup(800, 600)
screen.title("Challenge 7: Click-to-Draw")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(8)

# Customization variables
click_colors = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
current_color_index = 0
shape_size = 20

def click_handler(x, y):
    """This special function is called when someone clicks the screen"""
    global current_color_index  # This lets us change the color index
    
    # Move kheya to where the click happened (without drawing a line)
    kheya.penup()
    kheya.goto(x, y)
    kheya.pendown()
    
    # Change color for each click
    kheya.color(click_colors[current_color_index])
    current_color_index = (current_color_index + 1) % len(click_colors)
    
    # Your code here - what should kheya draw when someone clicks?
    # Ideas:
    # - kheya.circle(shape_size) to draw a circle
    # - kheya.dot(shape_size) to draw a solid dot
    # - Draw a small square or triangle
    # - Get creative with your click art!
    kheya.circle(shape_size)  # Example: Draw a small circle
    
    # Example: Draw a small circle
    # kheya.circle(shape_size)
    
    # Your drawing code here:
    

# Set up the click handling (this is advanced - don't worry about understanding it fully!)
screen.onclick(click_handler)

print("Click anywhere on the screen to draw!")
print("Each click will use a different color!")
print("Try clicking in different places to create art!")

# Keep the window open and listening for clicks
screen.listen()
screen.mainloop()