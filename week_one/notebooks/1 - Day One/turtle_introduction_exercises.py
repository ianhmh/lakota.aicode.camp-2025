"""
Turtle Graphics Introduction - Student Exercises
Fill in the function bodies to complete each drawing exercise.

This version keeps a single turtle screen open the whole time.
After each drawing you press Enter in the terminal to move on.
"""

import turtle

# ------------------------------------------------------------------
# GLOBALS
# ------------------------------------------------------------------
SCREEN_WIDTH, SCREEN_HEIGHT = 600, 400
screen = turtle.Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title("Turtle Graphics Examples")

# ------------------------------------------------------------------
# HELPER
# ------------------------------------------------------------------
def pause(msg="Press Enter to continue…"):
    """Pause between drawings without closing the turtle window."""
    input(msg)          # wait in the terminal
    screen.clear()      # wipe drawings, keep window open

# ------------------------------------------------------------------
# EXERCISES - FILL IN THE FUNCTION BODIES
# ------------------------------------------------------------------
def draw_line_example():
    """Draw a simple line moving forward 100 units."""
    screen.bgcolor("white")
    screen.title("Example 1: Simple Line")
    t = turtle.Turtle()
    t.speed(3)
    
    # TODO: Make the turtle move forward 100 units
    
    pause()

def draw_square_example():
    """Draw a square using a loop."""
    screen.bgcolor("lightblue")
    screen.title("Example 2: Square")
    t = turtle.Turtle()
    t.speed(5)

    # TODO: Use a loop to draw a square (4 sides, 90 degree turns)
    # Hint: forward(100) and left(90)
    
    pause()

def draw_square_with_variables():
    """Draw a square using variables for side length and turn angle."""
    screen.bgcolor("lightyellow")
    screen.title("Example 3: Square with Variables")
    t = turtle.Turtle()
    t.speed(6)

    side_length = 150
    turn_angle = 90

    # TODO: Use the variables above to draw a square with a loop
    
    pause()

def draw_colorful_triangle():
    """Draw a triangle with different colored sides."""
    screen.bgcolor("black")
    screen.title("Example 4: Colorful Triangle")
    t = turtle.Turtle()
    t.speed(4)
    t.pensize(3)

    colors = ["red", "green", "blue"]
    
    # TODO: Use a loop to draw a triangle, changing color for each side
    # Hint: Use t.color(color) and turn 120 degrees for triangles
    
    pause()

def draw_rectangle_exercise():
    """Draw a rectangle with different length and width."""
    screen.bgcolor("lightgreen")
    screen.title("Example 5: Rectangle")
    t = turtle.Turtle()
    t.speed(5)
    t.color("purple")
    t.pensize(2)

    length, width = 200, 100
    
    # TODO: Draw a rectangle using the length and width variables
    # Hint: A rectangle has 2 long sides and 2 short sides
    
    pause()

def creative_drawing_example():
    """Create a house with a base, roof, and door."""
    screen.bgcolor("navy")
    screen.title("Example 6: Creative House")
    t = turtle.Turtle()
    t.speed(7)
    t.color("yellow")
    t.pensize(2)

    # TODO: Draw a house with these components:
    # 1. Base square (100x100)
    # 2. Triangular roof on top (use t.goto() to position)
    # 3. A door in the front
    
    # Base square
    # TODO: Draw a 100x100 square
    
    # Roof
    # TODO: Move to position (-50, 100) and draw a triangle
    # Hint: Use t.penup(), t.goto(-50, 100), t.pendown()
    
    # Door
    # TODO: Move to position (25, 0) and draw a door
    # Hint: Draw a rectangle for the door
    
    pause("Click inside the turtle window to exit…")
    screen.exitonclick()     # close on final click

# ------------------------------------------------------------------
# MAIN
# ------------------------------------------------------------------
def main():
    print("Welcome to Turtle Graphics Exercises!\n"
          "Complete each function to draw the shapes.\n"
          "The turtle window stays open; press Enter in this terminal\n"
          "after each shape to see the next example.\n")

    draw_line_example()
    draw_square_example()
    draw_square_with_variables()
    draw_colorful_triangle()
    draw_rectangle_exercise()
    creative_drawing_example()

if __name__ == "__main__":
    main()