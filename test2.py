from p5 import *
import random

# Define the golden ratio
phi = (1 + 5 ** 0.5) / 2  # Approximately 1.618

def setup():
    size(800, 800)
    #no_loop()  # Draw once

def draw():
    background(255)
    
    # Get user input for the name
    name = input("Enter a name: ")
    create_pattern(name)

def create_pattern(name):
    # Set the starting position
    x, y = width / 2, height / 2
    spacing = 50  # Base space between shapes

    for char in name:
        draw_shape(char, x, y)
        # Update x position for the next shape using the golden ratio
        x += spacing * phi

        # Move to the next row if we go beyond the canvas width
        if x > width - 50:
            x = width / 2
            y += spacing * phi  # Use golden ratio for vertical spacing

def draw_shape(char, x, y):
    # Map characters to shapes
    if char.isalpha():
        # Use golden ratio to determine size
        size = random.randint(30, 60)
        fill(random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
        
        if char.lower() in 'aeiou':  # Vowels
            ellipse(x, y, size, size)
        else:  # Consonants
            rect(x - size / 2, y - size / 2, size, size)

def key_pressed():
    # Refresh the drawing on key press
    redraw()

run()