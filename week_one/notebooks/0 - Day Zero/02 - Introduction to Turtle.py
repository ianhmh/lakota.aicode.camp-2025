"""
Introduction to Turtle Graphics for High School Students
========================================================

Welcome to Python Turtle Graphics! This is a fun way to learn programming
by drawing pictures with code. Think of it like controlling a robot turtle
that can draw on a canvas.

This script will show you the basics of turtle graphics step by step.
Run each section and see what happens!
"""

import turtle
import time

# Create our turtle and set up the screen
print("🐢 Welcome to Turtle Graphics!")
print("Setting up our drawing canvas...")

# Create a screen (our canvas) and a turtle
screen = turtle.Screen()
screen.bgcolor("white")  # Set background color to white
screen.title("Introduction to Turtle Graphics")
screen.setup(width=800, height=600)  # Make our canvas 800x600 pixels

# Create our turtle - let's call him Keya!
keya = turtle.Turtle()
keya.shape("turtle")  # Make it look like a turtle
keya.color("blue")    # Make Keya blue
keya.speed(3)         # Set drawing speed (1=slow, 10=fast)

print("Meet Keya the Turtle! 🐢")
time.sleep(1)

# ============================================================================
# LESSON 1: Basic Movement
# ============================================================================
print("\n📚 LESSON 1: Basic Movement")
print("Let's teach Keya how to move around!")

# Move forward
print("- Moving forward 100 steps...")
keya.forward(100)
time.sleep(1)

# Turn right
print("- Turning right 90 degrees...")
keya.right(90)
time.sleep(1)

# Move forward again
print("- Moving forward 100 steps again...")
keya.forward(100)
time.sleep(1)

print("Great! Keya just drew two lines forming an 'L' shape!")

# ============================================================================
# LESSON 2: Drawing a Square
# ============================================================================
print("\n📚 LESSON 2: Drawing a Square")
print("Let's draw a complete square!")

# Clear the screen and start fresh
keya.clear()
keya.penup()    # Lift the pen so we don't draw while moving
keya.goto(-50, 50)  # Move to a starting position
keya.pendown()  # Put the pen down to start drawing

# Draw a square using a loop (this is more efficient than writing the same code 4 times!)
for side in range(4):  # Repeat 4 times (for 4 sides of a square)
    print(f"- Drawing side {side + 1} of the square...")
    keya.forward(100)  # Move forward 100 steps
    keya.right(90)     # Turn right 90 degrees
    time.sleep(0.5)

print("Perfect! Keya drew a square! 🟦")

# ============================================================================
# LESSON 3: Colors and Pen Control
# ============================================================================
print("\n📚 LESSON 3: Colors and Pen Control")
print("Let's add some color and learn about pen control!")

# Move to a new position without drawing
keya.penup()
keya.goto(50, 50)
keya.pendown()

# Change colors and draw
colors = ["red", "green", "blue", "orange", "purple"]

for i, color in enumerate(colors):
    print(f"- Drawing line {i + 1} in {color}...")
    keya.pencolor(color)  # Change pen color
    keya.forward(80)
    keya.right(72)  # 360 degrees ÷ 5 lines = 72 degrees
    time.sleep(0.5)

print("Wow! Keya drew a colorful star! ⭐")

# ============================================================================
# LESSON 4: Drawing a Flower
# ============================================================================
print("\n📚 LESSON 4: Drawing a Flower")
print("Let's create something more complex - a flower!")

# Clear and move to center
keya.clear()
keya.penup()
keya.goto(0, -100)
keya.pendown()

# Draw the stem
keya.pencolor("green")
keya.left(90)  # Point upward
keya.forward(200)

# Draw the flower petals
keya.pencolor("red")
for petal in range(8):  # 8 petals
    print(f"- Drawing petal {petal + 1}...")
    keya.circle(30)    # Draw a circle with radius 30
    keya.right(45)     # Turn 45 degrees (360 ÷ 8 = 45)
    time.sleep(0.3)

print("Beautiful! Keya drew a flower! 🌸")

# ============================================================================
# LESSON 5: Interactive Drawing
# ============================================================================
print("\n📚 LESSON 5: Your Turn!")
print("Now it's your turn to experiment!")
print("\nTry modifying the code below to create your own drawings:")
print("- Change the colors")
print("- Change the sizes")
print("- Add more shapes")
print("- Create patterns")

# Example: Draw a house
keya.clear()
keya.penup()
keya.goto(-100, -100)
keya.pendown()

# House base
keya.pencolor("brown")
for side in range(4):
    keya.forward(100)
    keya.right(90)

# Roof
keya.pencolor("red")
keya.goto(-100, 0)
keya.goto(-50, 50)  # Top of roof
keya.goto(0, 0)

# Door
keya.pencolor("blue")
keya.goto(-75, -100)
keya.left(90)
keya.forward(40)
keya.right(90)
keya.forward(20)
keya.right(90)
keya.forward(40)

print("Keya drew a house! 🏠")

# ============================================================================
# SUMMARY AND NEXT STEPS
# ============================================================================
print("\n🎉 Congratulations!")
print("You've learned the basics of turtle graphics!")
print("\nHere's what Keya can do:")
print("• terry.forward(distance) - Move forward")
print("• terry.backward(distance) - Move backward")
print("• terry.right(angle) - Turn right")
print("• terry.left(angle) - Turn left")
print("• terry.penup() - Stop drawing")
print("• terry.pendown() - Start drawing")
print("• terry.pencolor(color) - Change pen color")
print("• terry.circle(radius) - Draw a circle")
print("• terry.goto(x, y) - Move to specific position")
print("• terry.clear() - Clear the screen")

print("\n💡 Challenge Ideas:")
print("1. Draw your initials")
print("2. Create a rainbow")
print("3. Draw a spiral")
print("4. Make a geometric pattern")
print("5. Draw your favorite animal")

print("\nHave fun exploring turtle graphics! 🐢✨")

# Keep the window open so students can see the final result
print("\nClick on the turtle window to close it when you're done!")
screen.exitonclick()  # Close when clicked 