#!/usr/bin/env python3
"""
Turtle Decision Maker - Interactive Script for Day One Concepts
Reinforces: Data types, conditionals, and basic logic
"""

import turtle
import random

def setup_screen():
    """Set up the turtle graphics window"""
    screen = turtle.Screen()
    screen.title("Turtle Decision Maker - Data Types & Logic Practice")
    screen.bgcolor("lightblue")
    screen.setup(800, 600)
    return screen

def create_turtle():
    """Create and configure the turtle"""
    t = turtle.Turtle()
    t.speed(3)
    t.shape("turtle")
    return t

def get_user_input():
    """Get input from user and demonstrate data types"""
    print("\n🐢 TURTLE DECISION MAKER")
    print("=" * 30)
    
    # Get different types of input
    name = input("What's your name? ").strip()
    age_str = input("How old are you? ").strip()
    favorite_color = input("What's your favorite color? ").strip().lower()
    
    # Convert and validate age
    try:
        age = int(age_str)
        if age < 0 or age > 120:
            print("That seems like an unusual age! Using 16 instead.")
            age = 16
    except ValueError:
        print("That's not a valid number! Using 16 instead.")
        age = 16
    
    # Validate color
    valid_colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink", "black"]
    if favorite_color not in valid_colors:
        print(f"'{favorite_color}' isn't available. Using 'blue' instead.")
        favorite_color = "blue"
    
    return name, age, favorite_color

def make_turtle_decisions(t, name, age, favorite_color):
    """Make decisions based on user data - demonstrates conditionals"""
    
    print(f"\n🎯 Making decisions for {name} (age {age})...")
    
    # Decision 1: Turtle color based on age
    print("\n1. Choosing turtle color...")
    if age < 13:
        t.color("red")
        print("   Young person - energetic red!")
    elif age < 18:
        t.color(favorite_color)
        print(f"   Teen - your favorite color {favorite_color}!")
    elif age < 30:
        t.color("green")
        print("   Young adult - fresh green!")
    else:
        t.color("purple")
        print("   Mature - sophisticated purple!")
    
    # Decision 2: Drawing size based on age
    print("\n2. Choosing drawing size...")
    if age < 16:
        size = 50
        print("   Smaller drawings for younger artists")
    elif age < 25:
        size = 75
        print("   Medium drawings for developing skills")
    else:
        size = 100
        print("   Large drawings for experienced artists")
    
    # Decision 3: Drawing speed based on name length
    print("\n3. Setting drawing speed...")
    name_length = len(name)
    if name_length <= 4:
        speed = 1
        print(f"   Short name ({name_length} letters) - slow and careful")
    elif name_length <= 8:
        speed = 3
        print(f"   Medium name ({name_length} letters) - moderate speed")
    else:
        speed = 5
        print(f"   Long name ({name_length} letters) - quick and confident")
    
    t.speed(speed)
    
    return size

def draw_personalized_pattern(t, name, age, size):
    """Draw a pattern based on user characteristics"""
    
    print(f"\n🎨 Drawing personalized pattern...")
    
    # Choose pattern based on age
    if age < 15:
        pattern = "star"
        print("   Drawing a star pattern (youthful energy)")
    elif age < 25:
        pattern = "flower"
        print("   Drawing a flower pattern (growth and beauty)")
    else:
        pattern = "geometric"
        print("   Drawing geometric pattern (structured wisdom)")
    
    # Draw the chosen pattern
    if pattern == "star":
        draw_star(t, size)
    elif pattern == "flower":
        draw_flower(t, size)
    else:
        draw_geometric(t, size)
    
    # Add personalization based on name
    add_name_decoration(t, name, size)

def draw_star(t, size):
    """Draw a star pattern"""
    t.penup()
    t.goto(-size//2, 0)
    t.pendown()
    
    for _ in range(5):
        t.forward(size)
        t.right(144)

def draw_flower(t, size):
    """Draw a flower pattern"""
    t.penup()
    t.goto(0, 0)
    t.pendown()
    
    # Draw petals
    for _ in range(8):
        t.circle(size//2, 90)
        t.left(90)
        t.circle(size//2, 90)
        t.left(135)

def draw_geometric(t, size):
    """Draw a geometric pattern"""
    t.penup()
    t.goto(-size//2, -size//2)
    t.pendown()
    
    # Draw nested squares
    for i in range(4):
        square_size = size - (i * 15)
        for _ in range(4):
            t.forward(square_size)
            t.right(90)
        t.penup()
        t.forward(7.5)
        t.right(90)
        t.forward(7.5)
        t.left(90)
        t.pendown()

def add_name_decoration(t, name, size):
    """Add decoration based on name characteristics"""
    
    print(f"   Adding decoration based on name '{name}'...")
    
    # Count vowels in name
    vowels = "aeiou"
    vowel_count = sum(1 for char in name.lower() if char in vowels)
    
    # Draw dots around pattern based on vowel count
    t.penup()
    radius = size + 20
    
    for i in range(vowel_count * 2):  # More vowels = more dots
        angle = (360 / (vowel_count * 2)) * i
        x = radius * turtle.math.cos(turtle.math.radians(angle))
        y = radius * turtle.math.sin(turtle.math.radians(angle))
        t.goto(x, y)
        t.pendown()
        t.dot(8)
        t.penup()
    
    print(f"   Added {vowel_count * 2} decorative dots (based on {vowel_count} vowels in name)")

def demonstrate_data_types(name, age, favorite_color):
    """Show data type information"""
    
    print(f"\n📊 DATA TYPE ANALYSIS:")
    print(f"   Name: '{name}' (type: {type(name).__name__})")
    print(f"   Age: {age} (type: {type(age).__name__})")
    print(f"   Color: '{favorite_color}' (type: {type(favorite_color).__name__})")
    
    # Boolean demonstrations
    is_teen = 13 <= age <= 19
    is_adult = age >= 18
    has_long_name = len(name) > 6
    
    print(f"\n🔍 BOOLEAN ANALYSIS:")
    print(f"   Is teen (13-19): {is_teen} (type: {type(is_teen).__name__})")
    print(f"   Is adult (18+): {is_adult} (type: {type(is_adult).__name__})")
    print(f"   Has long name (>6 chars): {has_long_name} (type: {type(has_long_name).__name__})")
    
    # String operations demonstration
    print(f"\n📝 STRING OPERATIONS:")
    print(f"   Name length: {len(name)}")
    print(f"   Name uppercase: '{name.upper()}'")
    print(f"   Name reversed: '{name[::-1]}'")
    print(f"   First letter: '{name[0] if name else 'N/A'}'")

def create_data_summary(name, age, favorite_color):
    """Create a summary using different data types"""
    
    # Create lists of characteristics
    age_groups = ["child", "teen", "young adult", "adult", "senior"]
    personality_traits = []
    
    # Determine characteristics based on data
    if age < 13:
        age_group = age_groups[0]
        personality_traits.extend(["curious", "energetic"])
    elif age < 18:
        age_group = age_groups[1]
        personality_traits.extend(["creative", "adventurous"])
    elif age < 30:
        age_group = age_groups[2]
        personality_traits.extend(["ambitious", "innovative"])
    elif age < 60:
        age_group = age_groups[3]
        personality_traits.extend(["experienced", "wise"])
    else:
        age_group = age_groups[4]
        personality_traits.extend(["knowledgeable", "thoughtful"])
    
    # Add traits based on name
    if len(name) > 8:
        personality_traits.append("detailed-oriented")
    if len(name) <= 4:
        personality_traits.append("concise")
    
    # Color personality (just for fun)
    color_traits = {
        "red": "passionate",
        "blue": "calm",
        "green": "balanced",
        "yellow": "optimistic",
        "orange": "enthusiastic",
        "purple": "creative",
        "pink": "compassionate",
        "black": "sophisticated"
    }
    
    if favorite_color in color_traits:
        personality_traits.append(color_traits[favorite_color])
    
    print(f"\n🎭 PERSONALITY SUMMARY:")
    print(f"   {name} is a {age_group} who is {', '.join(personality_traits)}.")
    print(f"   Their favorite color {favorite_color} suggests they are {color_traits.get(favorite_color, 'unique')}.")
    
    return personality_traits

def main():
    """Main program that demonstrates Day One concepts"""
    
    print("🐢 TURTLE DECISION MAKER")
    print("This program demonstrates:")
    print("• Data types (str, int, bool)")
    print("• Conditional logic (if/elif/else)")
    print("• String operations and methods")
    print("• Type conversion and validation")
    print("• Boolean expressions and logic")
    
    # Set up graphics
    screen = setup_screen()
    t = create_turtle()
    
    # Get user input and demonstrate data types
    name, age, favorite_color = get_user_input()
    
    # Show data type analysis
    demonstrate_data_types(name, age, favorite_color)
    
    # Make decisions and draw
    size = make_turtle_decisions(t, name, age, favorite_color)
    draw_personalized_pattern(t, name, age, size)
    
    # Create personality summary
    traits = create_data_summary(name, age, favorite_color)
    
    # Final message
    print(f"\n✨ COMPLETE!")
    print(f"Your personalized turtle art has been created!")
    print(f"It reflects your age ({age}), your name ('{name}'), and your style.")
    print(f"\n🎯 Programming concepts demonstrated:")
    print(f"• Data type conversion: '{age}' (string) → {age} (integer)")
    print(f"• String validation: checking if '{favorite_color}' is valid")
    print(f"• Conditional logic: different patterns for different ages")
    print(f"• Boolean expressions: is_teen = {13 <= age <= 19}")
    print(f"• List operations: personality traits = {traits}")
    
    # Wait for click to close
    print(f"\n👆 Click the turtle window to close...")
    screen.exitonclick()

if __name__ == "__main__":
    main()