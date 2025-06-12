"""
Challenge 4: Draw a Simple Tree
Create a tree with branches using loops and conditionals.
Your turtle friend is named kheya!

Concepts used: Variables, loops, conditionals, positioning
NOTE: This is a simplified version without recursion
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("lightblue")
screen.setup(800, 800)
screen.title("Challenge 4: Draw a Simple Tree")

# Meet kheya, your turtle friend!
kheya = turtle.Turtle()
kheya.speed(6)
kheya.color("brown")

# Tree customization variables - change these to modify your tree!
trunk_length = 100      # Length of the main trunk
trunk_color = "brown"   # Color of the trunk
branch_color = "green"  # Color of the branches
branch_length = 50      # Length of each branch
num_branches = 6        # Number of branches

# Starting position
start_x = 0
start_y = -200

# Move to starting position and point upward
kheya.penup()
kheya.goto(start_x, start_y)
kheya.pendown()
kheya.setheading(90)  # Point straight up

# Draw the trunk
kheya.color(trunk_color)
kheya.forward(trunk_length)

# Now draw branches
kheya.color(branch_color)

# Your code here - draw branches coming off the trunk
# Ideas for branches:
# 1. Simple approach: Draw lines going left and right at different heights
# 2. Use a loop to draw multiple branches
# 3. Use conditionals to make some branches longer than others

# Example structure:
# for i in range(num_branches):
#     # Calculate where this branch should be
#     # Move to that position
#     # Draw a branch going left
#     # Go back to trunk
#     # Draw a branch going right
#     # Move up the trunk for the next branch

# Here's a starter template - fill in the details:
for i in range(num_branches):
    # Move partway up the trunk for this branch
    branch_height = (trunk_length // num_branches) * i
    
    # Go to the branch position
    kheya.penup()
    kheya.goto(start_x, start_y + branch_height)
    kheya.pendown()
    
    # Draw left branch
    kheya.setheading(135)  # Point up and left
    # Your code: draw the left branch
    kheya.forward(branch_length)
    # Optional: Add some randomness to branch length or angle
    kheya.backward(branch_length)  # Go back to trunk
    kheya.setheading(90)  # Point straight up again
    kheya.penup()
    kheya.goto(start_x, start_y + branch_height)  # Go back to trunk position
    kheya.pendown()
    kheya.setheading(45)   # Point up and right
    
    
    # Go back to trunk
    kheya.penup()
    kheya.goto(start_x, start_y + branch_height)
    kheya.pendown()
    
    # Draw right branch  
    kheya.setheading(45)   # Point up and right
    # Your code: draw the right branch
    

# Keep the window open
screen.exitonclick()
print("Click the screen to close!")