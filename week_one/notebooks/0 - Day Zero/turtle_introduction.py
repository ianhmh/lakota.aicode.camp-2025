"""
Turtle Graphics Introduction
A Python script demonstrating basic turtle graphics concepts

This script shows the difference between Jupyter notebooks and Python scripts.
Unlike notebooks, scripts run all at once from top to bottom.

Learning objectives:
- Understand import statements and libraries
- Practice giving precise instructions to a computer
- Learn basic turtle commands
- See programming as visual instructions
- Understand the difference between scripts and notebooks
"""

# Import the turtle library - this lets us use turtle graphics
import turtle

def draw_line_example():
    """Example 1: Drawing a simple line"""
    print("Example 1: Drawing a simple line")
    
    # Create a screen (canvas) and a turtle
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.title("Example 1: Simple Line")
    screen.setup(width=600, height=400)
    
    # Create our turtle
    line_turtle = turtle.Turtle()
    line_turtle.speed(3)  # 1=slow, 10=fast
    
    # Draw a line
    line_turtle.forward(100)
    
    # Wait for user to click before continuing
    print("Click on the window to continue to the next example...")
    screen.exitonclick()

def draw_square_example():
    """Example 2: Drawing a square step by step"""
    print("Example 2: Drawing a square")
    
    # Create a new screen for this example
    screen = turtle.Screen()
    screen.bgcolor("lightblue")
    screen.title("Example 2: Drawing a Square")
    screen.setup(width=600, height=400)
    
    square_turtle = turtle.Turtle()
    square_turtle.speed(5)
    
    # Draw a square - notice the pattern!
    square_turtle.forward(100)  # Side 1
    square_turtle.left(90)      # Turn corner
    square_turtle.forward(100)  # Side 2
    square_turtle.left(90)      # Turn corner
    square_turtle.forward(100)  # Side 3
    square_turtle.left(90)      # Turn corner
    square_turtle.forward(100)  # Side 4
    square_turtle.left(90)      # Turn corner (back to start)
    
    print("Click on the window to continue to the next example...")
    screen.exitonclick()

def draw_square_with_variables():
    """Example 3: Using variables to make our square customizable"""
    print("Example 3: Square with variables")
    
    screen = turtle.Screen()
    screen.bgcolor("lightyellow")
    screen.title("Example 3: Customizable Square")
    screen.setup(width=600, height=400)
    
    my_turtle = turtle.Turtle()
    my_turtle.speed(6)
    
    # Variables make our code flexible!
    side_length = 150
    turn_angle = 90
    
    # Draw the square using variables
    my_turtle.forward(side_length)
    my_turtle.left(turn_angle)
    my_turtle.forward(side_length)
    my_turtle.left(turn_angle)
    my_turtle.forward(side_length)
    my_turtle.left(turn_angle)
    my_turtle.forward(side_length)
    my_turtle.left(turn_angle)
    
    print("Click on the window to continue to the next example...")
    screen.exitonclick()

def draw_colorful_triangle():
    """Example 4: Adding color to our drawings"""
    print("Example 4: Colorful triangle")
    
    screen = turtle.Screen()
    screen.bgcolor("black")
    screen.title("Example 4: Colorful Triangle")
    screen.setup(width=600, height=400)
    
    color_turtle = turtle.Turtle()
    color_turtle.speed(4)
    color_turtle.pensize(3)  # Make the line thicker
    
    # Draw a triangle with different colored sides
    color_turtle.color("red")
    color_turtle.forward(120)
    color_turtle.left(120)
    
    color_turtle.color("green")
    color_turtle.forward(120)
    color_turtle.left(120)
    
    color_turtle.color("blue")
    color_turtle.forward(120)
    color_turtle.left(120)
    
    print("Click on the window to continue to the next example...")
    screen.exitonclick()

def draw_rectangle_exercise():
    """Example 5: Rectangle drawing exercise"""
    print("Example 5: Drawing a rectangle")
    
    screen = turtle.Screen()
    screen.bgcolor("lightgreen")
    screen.title("Example 5: Rectangle")
    screen.setup(width=600, height=400)
    
    rect_turtle = turtle.Turtle()
    rect_turtle.speed(5)
    rect_turtle.color("purple")
    rect_turtle.pensize(2)
    
    # Rectangle has two different side lengths
    length = 200
    width = 100
    
    # Draw rectangle
    rect_turtle.forward(length)
    rect_turtle.left(90)
    rect_turtle.forward(width)
    rect_turtle.left(90)
    rect_turtle.forward(length)
    rect_turtle.left(90)
    rect_turtle.forward(width)
    rect_turtle.left(90)
    
    print("Click on the window to continue to the next example...")
    screen.exitonclick()

def creative_drawing_example():
    """Example 6: A more creative drawing using pen up/down"""
    print("Example 6: Creative drawing with pen up/down")
    
    screen = turtle.Screen()
    screen.bgcolor("navy")
    screen.title("Example 6: Creative Drawing")
    screen.setup(width=600, height=400)
    
    artist = turtle.Turtle()
    artist.speed(7)
    artist.color("yellow")
    artist.pensize(2)
    
    # Draw a simple house
    # First, draw the base (square)
    for _ in range(4):
        artist.forward(100)
        artist.left(90)
    
    # Move to draw the roof (triangle)
    artist.penup()  # Stop drawing
    artist.goto(-50, 100)  # Move to new position
    artist.pendown()  # Start drawing again
    
    # Draw triangle roof
    artist.color("red")
    for _ in range(3):
        artist.forward(100)
        artist.left(120)
    
    # Add a door
    artist.penup()
    artist.goto(25, 0)
    artist.pendown()
    artist.color("brown")
    artist.left(90)
    artist.forward(50)
    artist.right(90)
    artist.forward(25)
    artist.right(90)
    artist.forward(50)
    
    print("Click on the window to finish!")
    screen.exitonclick()

def main():
    """
    Main function that runs all our examples
    
    This is a common pattern in Python scripts - having a main() function
    that controls the flow of the program.
    """
    print("Welcome to Turtle Graphics!")
    print("This script will show you several examples of turtle drawings.")
    print("Each example will open in a new window.")
    print("Click on each window when you're ready to continue.\n")
    
    # Run all our examples in order
    draw_line_example()
    draw_square_example()
    draw_square_with_variables()
    draw_colorful_triangle()
    draw_rectangle_exercise()
    creative_drawing_example()
    
    print("\nGreat job! You've completed all the turtle examples.")
    print("Now try modifying this script to create your own drawings!")

# This is a special Python pattern - it means "only run main() if this script
# is being run directly, not if it's being imported by another script"
if __name__ == "__main__":
    main()


"""
TURTLE COMMAND REFERENCE:

Movement Commands:
- turtle.forward(distance) or turtle.fd(distance)
- turtle.backward(distance) or turtle.bk(distance)
- turtle.left(angle) or turtle.lt(angle)
- turtle.right(angle) or turtle.rt(angle)

Pen Control:
- turtle.penup() or turtle.pu() - stop drawing
- turtle.pendown() or turtle.pd() - start drawing
- turtle.pensize(width) - change line thickness

Color and Style:
- turtle.color(color_name) - change pen color
- turtle.bgcolor(color_name) - change background color

Position:
- turtle.home() - return to center (0, 0)
- turtle.goto(x, y) - move to specific coordinates

Speed:
- turtle.speed(number) - set drawing speed (1=slow, 10=fast)

Screen Control:
- screen.exitonclick() - close window when clicked
- screen.setup(width, height) - set window size

EXERCISES TO TRY:
1. Change the colors in any of the examples
2. Make the shapes bigger or smaller by changing the numbers
3. Try drawing a hexagon (6 sides, 60-degree turns)
4. Create your own house design
5. Draw your initials using turtle graphics
6. Make a pattern by drawing multiple shapes
"""