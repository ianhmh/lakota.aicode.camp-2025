#!/usr/bin/env python3
"""
Turtle List Processor - Interactive Script for Day One Concepts
Reinforces: Lists, loops, and automation
"""

import turtle
import random
import time

def setup_screen():
    """Set up the turtle graphics window"""
    screen = turtle.Screen()
    screen.title("Turtle List Processor - Lists & Loops Practice")
    screen.bgcolor("black")
    screen.setup(900, 700)
    return screen

def create_turtle():
    """Create and configure the turtle"""
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    t.shape("turtle")
    t.color("white")
    return t

def demonstrate_list_basics():
    """Introduce list concepts with examples"""
    
    print("\n🐢 TURTLE LIST PROCESSOR")
    print("=" * 35)
    print("This program demonstrates:")
    print("• Creating and modifying lists")
    print("• Accessing list elements by index")
    print("• Using loops to process lists")
    print("• Combining lists with graphics")
    
    # Create sample lists
    colors = ["red", "blue", "green", "yellow", "orange", "purple", "pink"]
    sizes = [20, 30, 40, 50, 60, 70, 80]
    shapes = ["circle", "square", "triangle", "star", "hexagon"]
    
    print(f"\n📝 SAMPLE LISTS:")
    print(f"Colors: {colors}")
    print(f"Sizes: {sizes}")
    print(f"Shapes: {shapes}")
    
    print(f"\n🔍 LIST ANALYSIS:")
    print(f"Colors list has {len(colors)} items")
    print(f"First color: {colors[0]}")
    print(f"Last color: {colors[-1]}")
    print(f"Middle color: {colors[len(colors)//2]}")
    
    return colors, sizes, shapes

def get_user_preferences():
    """Get user's drawing preferences"""
    
    print(f"\n🎨 CUSTOMIZATION:")
    
    # Get drawing preferences
    try:
        num_shapes = int(input("How many shapes to draw (3-20)? "))
        if num_shapes < 3:
            num_shapes = 3
        elif num_shapes > 20:
            num_shapes = 20
    except ValueError:
        num_shapes = 8
        print("Using default: 8 shapes")
    
    pattern_choice = input("Pattern type (spiral/circle/grid/random)? ").lower().strip()
    valid_patterns = ["spiral", "circle", "grid", "random"]
    if pattern_choice not in valid_patterns:
        pattern_choice = "spiral"
        print(f"Using default: {pattern_choice}")
    
    use_random_colors = input("Use random colors (y/n)? ").lower().strip()
    random_colors = use_random_colors in ["y", "yes", "true", "1"]
    
    return num_shapes, pattern_choice, random_colors

def create_drawing_data(colors, sizes, shapes, num_shapes, random_colors):
    """Create lists of drawing instructions"""
    
    print(f"\n🎯 GENERATING DRAWING DATA...")
    
    # Create lists for the drawing
    shape_list = []
    color_list = []
    size_list = []
    position_list = []
    
    for i in range(num_shapes):
        # Choose shape (cycle through available shapes)
        shape = shapes[i % len(shapes)]
        shape_list.append(shape)
        
        # Choose color
        if random_colors:
            color = random.choice(colors)
        else:
            color = colors[i % len(colors)]
        color_list.append(color)
        
        # Choose size (gradually increasing)
        base_size = 20 + (i * 5)
        if base_size > 80:
            base_size = 20 + ((i % 12) * 5)
        size_list.append(base_size)
        
        # Position will be calculated later based on pattern
        position_list.append((0, 0))  # Placeholder
    
    print(f"Created lists with {len(shape_list)} items each:")
    print(f"  Shapes: {shape_list}")
    print(f"  Colors: {color_list}")
    print(f"  Sizes: {size_list[:5]}{'...' if len(size_list) > 5 else ''}")
    
    return shape_list, color_list, size_list, position_list

def calculate_positions(pattern_choice, num_shapes):
    """Calculate positions based on pattern choice"""
    
    positions = []
    
    if pattern_choice == "spiral":
        print("📐 Calculating spiral positions...")
        for i in range(num_shapes):
            angle = i * 25  # Degrees
            radius = i * 15
            x = radius * turtle.math.cos(turtle.math.radians(angle))
            y = radius * turtle.math.sin(turtle.math.radians(angle))
            positions.append((x, y))
    
    elif pattern_choice == "circle":
        print("📐 Calculating circular positions...")
        radius = 150
        for i in range(num_shapes):
            angle = (360 / num_shapes) * i
            x = radius * turtle.math.cos(turtle.math.radians(angle))
            y = radius * turtle.math.sin(turtle.math.radians(angle))
            positions.append((x, y))
    
    elif pattern_choice == "grid":
        print("📐 Calculating grid positions...")
        cols = int(turtle.math.sqrt(num_shapes)) + 1
        spacing = 100
        start_x = -(cols * spacing) // 2
        start_y = -(cols * spacing) // 2
        
        for i in range(num_shapes):
            row = i // cols
            col = i % cols
            x = start_x + (col * spacing)
            y = start_y + (row * spacing)
            positions.append((x, y))
    
    else:  # random
        print("📐 Calculating random positions...")
        for i in range(num_shapes):
            x = random.randint(-300, 300)
            y = random.randint(-250, 250)
            positions.append((x, y))
    
    return positions

def draw_shape(t, shape, size):
    """Draw a specific shape"""
    
    if shape == "circle":
        t.circle(size // 2)
    
    elif shape == "square":
        for _ in range(4):
            t.forward(size)
            t.right(90)
    
    elif shape == "triangle":
        for _ in range(3):
            t.forward(size)
            t.right(120)
    
    elif shape == "hexagon":
        for _ in range(6):
            t.forward(size // 2)
            t.right(60)
    
    elif shape == "star":
        for _ in range(5):
            t.forward(size)
            t.right(144)
    
    else:  # default to circle
        t.circle(size // 2)

def process_drawing_lists(t, shape_list, color_list, size_list, position_list):
    """Process all lists simultaneously to create the drawing"""
    
    print(f"\n🎨 PROCESSING LISTS...")
    print(f"Drawing {len(shape_list)} shapes using parallel lists...")
    
    # Statistics tracking
    shapes_drawn = 0
    total_perimeter = 0
    color_count = {}
    shape_count = {}
    
    # Process each item in the lists
    for i in range(len(shape_list)):
        shape = shape_list[i]
        color = color_list[i]
        size = size_list[i]
        x, y = position_list[i]
        
        print(f"  Drawing {i+1}: {shape} in {color} (size {size}) at ({x:.0f}, {y:.0f})")
        
        # Move turtle to position
        t.penup()
        t.goto(x, y)
        t.pendown()
        
        # Set color
        t.color(color)
        
        # Draw shape
        draw_shape(t, shape, size)
        
        # Update statistics
        shapes_drawn += 1
        total_perimeter += size * 4  # Rough estimate
        
        # Count colors and shapes
        if color in color_count:
            color_count[color] += 1
        else:
            color_count[color] = 1
        
        if shape in shape_count:
            shape_count[shape] += 1
        else:
            shape_count[shape] = 1
        
        # Small delay for visual effect
        time.sleep(0.1)
    
    return shapes_drawn, total_perimeter, color_count, shape_count

def analyze_drawing_statistics(shape_list, color_list, size_list, color_count, shape_count):
    """Analyze the drawing data using list operations"""
    
    print(f"\n📊 DRAWING STATISTICS:")
    print(f"=" * 25)
    
    # Basic list statistics
    total_shapes = len(shape_list)
    unique_colors = len(color_count)
    unique_shapes = len(shape_count)
    
    print(f"Total shapes drawn: {total_shapes}")
    print(f"Unique colors used: {unique_colors}")
    print(f"Unique shape types: {unique_shapes}")
    
    # Size analysis
    smallest_size = min(size_list)
    largest_size = max(size_list)
    average_size = sum(size_list) / len(size_list)
    
    print(f"\nSize Analysis:")
    print(f"  Smallest: {smallest_size}")
    print(f"  Largest: {largest_size}")
    print(f"  Average: {average_size:.1f}")
    
    # Color frequency
    print(f"\nColor Frequency:")
    for color, count in color_count.items():\n        percentage = (count / total_shapes) * 100\n        print(f\"  {color}: {count} times ({percentage:.1f}%)\")\n    \n    # Shape frequency\n    print(f\"\\nShape Frequency:\")\n    for shape, count in shape_count.items():\n        percentage = (count / total_shapes) * 100\n        print(f\"  {shape}: {count} times ({percentage:.1f}%)\")\n    \n    # Find most/least common\n    most_common_color = max(color_count, key=color_count.get)\n    most_common_shape = max(shape_count, key=shape_count.get)\n    \n    print(f\"\\n🏆 Most common:\")\n    print(f\"  Color: {most_common_color} ({color_count[most_common_color]} times)\")\n    print(f\"  Shape: {most_common_shape} ({shape_count[most_common_shape]} times)\")\n\ndef demonstrate_list_operations():\n    \"\"\"Show various list operations\"\"\"\n    \n    print(f\"\\n🔧 LIST OPERATIONS DEMO:\")\n    \n    # Create sample data\n    numbers = [5, 2, 8, 1, 9, 3]\n    words = [\"turtle\", \"graphics\", \"python\", \"code\"]\n    \n    print(f\"Original numbers: {numbers}\")\n    print(f\"Original words: {words}\")\n    \n    # Sorting\n    sorted_numbers = numbers.copy()  # Make a copy to preserve original\n    sorted_numbers.sort()\n    print(f\"Sorted numbers: {sorted_numbers}\")\n    \n    sorted_words = words.copy()\n    sorted_words.sort()\n    print(f\"Sorted words: {sorted_words}\")\n    \n    # Filtering with loops\n    large_numbers = []\n    for num in numbers:\n        if num > 5:\n            large_numbers.append(num)\n    print(f\"Numbers > 5: {large_numbers}\")\n    \n    long_words = []\n    for word in words:\n        if len(word) > 4:\n            long_words.append(word)\n    print(f\"Words > 4 letters: {long_words}\")\n    \n    # Transforming data\n    doubled_numbers = []\n    for num in numbers:\n        doubled_numbers.append(num * 2)\n    print(f\"Doubled numbers: {doubled_numbers}\")\n    \n    uppercase_words = []\n    for word in words:\n        uppercase_words.append(word.upper())\n    print(f\"Uppercase words: {uppercase_words}\")\n\ndef create_interactive_menu(t, colors, shapes):\n    \"\"\"Create an interactive menu for additional drawings\"\"\"\n    \n    print(f\"\\n🎮 INTERACTIVE MODE:\")\n    print(\"Choose additional drawings:\")\n    print(\"1. Random color explosion\")\n    print(\"2. Size progression demo\")\n    print(\"3. Shape transformation\")\n    print(\"4. Color gradient effect\")\n    print(\"5. Skip interactive mode\")\n    \n    try:\n        choice = int(input(\"Enter choice (1-5): \"))\n    except ValueError:\n        choice = 5\n    \n    if choice == 1:\n        random_explosion(t, colors)\n    elif choice == 2:\n        size_progression(t, colors)\n    elif choice == 3:\n        shape_transformation(t, shapes)\n    elif choice == 4:\n        color_gradient(t)\n    else:\n        print(\"Skipping interactive mode...\")\n\ndef random_explosion(t, colors):\n    \"\"\"Draw random dots in random colors\"\"\"\n    print(\"Creating random color explosion...\")\n    \n    dot_count = 50\n    positions = []\n    chosen_colors = []\n    \n    # Generate random positions and colors\n    for i in range(dot_count):\n        x = random.randint(-350, 350)\n        y = random.randint(-250, 250)\n        color = random.choice(colors)\n        positions.append((x, y))\n        chosen_colors.append(color)\n    \n    # Draw all dots\n    for i in range(dot_count):\n        x, y = positions[i]\n        color = chosen_colors[i]\n        \n        t.penup()\n        t.goto(x, y)\n        t.color(color)\n        t.dot(random.randint(5, 15))\n        \n        if i % 10 == 0:  # Print progress\n            print(f\"  Drew {i+1}/{dot_count} dots...\")\n    \n    print(f\"✨ Drew {dot_count} random dots!\")\n\ndef size_progression(t, colors):\n    \"\"\"Show size progression with same shape\"\"\"\n    print(\"Creating size progression...\")\n    \n    sizes = [10, 20, 30, 40, 50, 60, 70, 80]\n    x_positions = [-300, -200, -100, 0, 100, 200, 300, 400]\n    \n    for i in range(len(sizes)):\n        if i < len(x_positions):\n            t.penup()\n            t.goto(x_positions[i], 0)\n            t.pendown()\n            t.color(colors[i % len(colors)])\n            \n            # Draw circle with increasing size\n            t.circle(sizes[i] // 2)\n            print(f\"  Drew circle size {sizes[i]}\")\n    \n    print(\"✨ Size progression complete!\")\n\ndef shape_transformation(t, shapes):\n    \"\"\"Show different shapes in sequence\"\"\"\n    print(\"Creating shape transformation...\")\n    \n    positions = [(0, 100), (100, 50), (100, -50), (0, -100), (-100, -50), (-100, 50)]\n    \n    for i in range(min(len(shapes), len(positions))):\n        x, y = positions[i]\n        shape = shapes[i]\n        \n        t.penup()\n        t.goto(x, y)\n        t.pendown()\n        t.color(\"white\")\n        \n        draw_shape(t, shape, 40)\n        print(f\"  Drew {shape} at ({x}, {y})\")\n    \n    print(\"✨ Shape transformation complete!\")\n\ndef color_gradient(t):\n    \"\"\"Create a color gradient effect\"\"\"\n    print(\"Creating color gradient...\")\n    \n    # RGB color progression\n    colors = [(1.0, 0.0, 0.0), (1.0, 0.5, 0.0), (1.0, 1.0, 0.0), \n              (0.5, 1.0, 0.0), (0.0, 1.0, 0.0), (0.0, 1.0, 0.5),\n              (0.0, 1.0, 1.0), (0.0, 0.5, 1.0), (0.0, 0.0, 1.0),\n              (0.5, 0.0, 1.0), (1.0, 0.0, 1.0), (1.0, 0.0, 0.5)]\n    \n    positions = []\n    for i in range(len(colors)):\n        angle = (360 / len(colors)) * i\n        x = 150 * turtle.math.cos(turtle.math.radians(angle))\n        y = 150 * turtle.math.sin(turtle.math.radians(angle))\n        positions.append((x, y))\n    \n    for i in range(len(colors)):\n        x, y = positions[i]\n        r, g, b = colors[i]\n        \n        t.penup()\n        t.goto(x, y)\n        t.color(r, g, b)\n        t.dot(30)\n        \n        print(f\"  Drew gradient dot {i+1}/{len(colors)}\")\n    \n    print(\"✨ Color gradient complete!\")\n\ndef main():\n    \"\"\"Main program demonstrating lists and loops\"\"\"\n    \n    # Setup\n    screen = setup_screen()\n    t = create_turtle()\n    \n    # Demonstrate list basics\n    colors, sizes, shapes = demonstrate_list_basics()\n    \n    # Get user preferences\n    num_shapes, pattern_choice, random_colors = get_user_preferences()\n    \n    # Create drawing data\n    shape_list, color_list, size_list, position_list = create_drawing_data(\n        colors, sizes, shapes, num_shapes, random_colors)\n    \n    # Calculate positions\n    position_list = calculate_positions(pattern_choice, num_shapes)\n    \n    # Process lists and draw\n    shapes_drawn, total_perimeter, color_count, shape_count = process_drawing_lists(\n        t, shape_list, color_list, size_list, position_list)\n    \n    # Analyze statistics\n    analyze_drawing_statistics(shape_list, color_list, size_list, color_count, shape_count)\n    \n    # Demonstrate list operations\n    demonstrate_list_operations()\n    \n    # Interactive menu\n    create_interactive_menu(t, colors, shapes)\n    \n    # Summary\n    print(f\"\\n✨ PROGRAM COMPLETE!\")\n    print(f\"\\n🎯 Programming concepts demonstrated:\")\n    print(f\"• List creation: {len(shape_list)} items in parallel lists\")\n    print(f\"• List indexing: accessing items by position [0], [1], [-1]\")\n    print(f\"• For loops: processing {shapes_drawn} items automatically\")\n    print(f\"• List methods: .append(), .count(), min(), max(), sum()\")\n    print(f\"• Data analysis: frequency counting and statistics\")\n    print(f\"• Pattern recognition: {pattern_choice} layout algorithm\")\n    \n    print(f\"\\n👆 Click the turtle window to close...\")\n    screen.exitonclick()\n\nif __name__ == \"__main__\":\n    main()