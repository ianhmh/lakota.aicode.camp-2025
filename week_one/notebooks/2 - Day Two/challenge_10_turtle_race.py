"""
Challenge 10: Turtle Race (Advanced Challenge)
Create multiple turtles that race across the screen.
Your turtle friend kheya will compete with other turtles!

Concepts used: Variables, loops, conditionals, lists, randomness
NOTE: This challenge uses some advanced concepts but is mostly complete!
"""

import turtle

# Create our turtle and screen
screen = turtle.Screen()
screen.bgcolor("lightgreen")
screen.setup(800, 600)
screen.title("Challenge 10: Turtle Race")

# Race customization variables
num_racers = 4
race_distance = 600  # How far across the screen
start_x = -300       # Starting line x position
finish_x = 300       # Finish line x position

# Colors for the racing turtles
racer_colors = ["red", "blue", "green", "yellow", "purple", "orange"]

# Create the racing turtles
racers = []

print("Setting up the turtle race...")

# Create kheya as the first racer (red turtle)
kheya = turtle.Turtle()
kheya.shape("turtle")
kheya.color("red")
kheya.speed(1)
kheya.penup()
kheya.goto(start_x, 100)
racers.append(kheya)

# Create the other racing turtles
for i in range(1, num_racers):
    racer = turtle.Turtle()
    racer.shape("turtle")
    racer.color(racer_colors[i % len(racer_colors)])
    racer.speed(1)
    racer.penup()
    
    # Position each turtle at a different height
    start_y = 100 - (i * 40)
    racer.goto(start_x, start_y)
    
    racers.append(racer)

# Draw the finish line
finish_line = turtle.Turtle()
finish_line.speed(0)
finish_line.penup()
finish_line.goto(finish_x, 200)
finish_line.pendown()
finish_line.setheading(270)  # Point down
finish_line.pensize(5)
finish_line.color("black")
finish_line.forward(400)  # Draw vertical line
finish_line.hideturtle()

print("Racers ready!")
print("Kheya is the red turtle in lane 1!")
print("Press Enter to start the race!")
input()

# Run the race!
race_ongoing = True
step = 0

while race_ongoing:
    step += 1
    print(f"Race step {step}...")
    
    # Move each racer forward by a random amount
    for i, racer in enumerate(racers):
        # Your code here - make each racer move forward
        # Ideas:
        # - Use racer.forward() with a random distance
        # - Try different amounts like: 5, 10, 15, or random numbers
        # - Maybe some turtles move faster than others?
        
        # Simple version: each turtle moves 10 units
        # racer.forward(10)
        
        # Random version: each turtle moves a random distance
        # import random  # (already imported above)
        # move_distance = random.randint(5, 15)
        # racer.forward(move_distance)
        
        # Your movement code here:
        racer.forward(10)  # Replace this with your code!
        
        # Check if this racer won
        if racer.xcor() >= finish_x:
            winner_color = racer.color()[0]
            if i == 0:  # kheya (first racer)
                print(f"🎉 KHEYA WINS! The {winner_color} turtle is victorious! 🎉")
            else:
                print(f"The {winner_color} turtle wins!")
            race_ongoing = False
            break
    
    # Small pause between steps (optional)
    screen.update()

print("Race finished!")
print("Click the screen to close!")
screen.exitonclick()