#!/bin/python3

#from p5 import image, fill, rect, load_image, no_stroke, run, size, Color, save_canvas, redraw, rect_mode, square
from p5 import *
from random import randint, seed

# Draw a planet based on chosen size and colour
def shape_1(size, colour): 
  
    x = randint(0, 400)
    y = randint(0, 400)
    if colour == 'purple':
        image(purple_planet, x, y, size, size)
    elif colour == 'orange':
        image(orange_planet, x, y, size, size)
    elif colour == 'green':
        image(green_planet, x, y, size, size)
    elif colour == 'grey':
        image(grey_moon, x, y, size, size)
  
# Draw a space object based on chosen object and size
def shape_2(size, object): 
  
    x = randint(0, 400)
    y = randint(0, 400)
    if object == 'satellite':
        image(satellite, x, y, size, size)
    elif object == 'astronaut':
        image(astronaut, x, y, size, size)
    elif object == 'astropi':
        image(astropi, x, y, size, size)

# Draw a star based on chosen colour and size
def shape_3(size, colour): 
  
    x = randint(0, 400)
    y = randint(0, 400)
    if colour == 'yellow':
        image(yellow_star, x, y, size, size)
    elif colour == 'pink':
        image(pink_star, x, y, size, size)
    elif colour == 'blue':
        image(blue_star, x, y, size, size)

# Adds a background colour
def draw_background():
  
    # Background colour
    #fill(Color(255, 255, 255)) #white
    fill(Color(0,0,0)) #black
    rect(0, 0, 400, 666)

def setup():
  
    # Allow other functions to access the images
    global purple_planet, orange_planet, green_planet, astropi, astronaut, satellite 
    global grey_moon, yellow_star, pink_star, blue_star
    global pat1, pat2, pat3, pat4, pat5, pat6, pat7, pat8, pat9, logo

    size(400, 666)

    # Load the images needed into variables
    logo = load_image('logo.png')
    pat2 = load_image('pat2.png')
    pat3 = load_image('pat3.png')
    pat4 = load_image('pat4.png')
    pat5 = load_image('pat5.png')
    pat6 = load_image('pat6.png')
    pat7 = load_image('pat7.png')
    pat8 = load_image('pat8.png')
    pat9 = load_image('pat9.png')
    pat1 = load_image('pat1.png')

  
def draw():
    name = input("Enter a name: ")
    # Dictionary of letters and their encoded shape
    # code = {
    #     # letter [shape, size, colour]
    #     'a': ['shape 3', 50, 'pink'],
    #     'b': ['shape 3', 50, 'yellow'],
    #     'c': ['shape 2', 50, 'astronaut'],
    #     'd': ['shape 2', 50, 'astropi'],
    #     'e': ['shape 1', 50, 'orange'],
    #     'f': ['shape 2', 50, 'satellite'],
    #     'g': ['shape 1', 50, 'purple'],
    #     'h': ['shape 1', 50, 'green'],
    #     'i': ['shape 1', 50, 'orange'],
    #     'j': ['shape 2', 50, 'astropi'],
    #     'k': ['shape 1', 50, 'purple'],
    #     'l': ['shape 3', 50, 'pink'],
    #     'm': ['shape 1', 50, 'orange'],
    #     'n': ['shape 1', 50, 'green'],
    #     'o': ['shape 3', 50, 'blue'],
    #     'p': ['shape 2', 50, 'astropi'],
    #     'q': ['shape 3', 50, 'blue'],
    #     'r': ['shape 1', 50, 'purple'],
    #     's': ['shape 1', 50, 'orange'],
    #     't': ['shape 2', 50, 'astronaut'],
    #     'u': ['shape 1', 50, 'grey'],
    #     'v': ['shape 3', 50, 'yellow'],
    #     'w': ['shape 1', 50, 'orange'],
    #     'x': ['shape 2', 50, 'astropi'],
    #     'y': ['shape 1', 50, 'purple'],
    #     'z': ['shape 2', 50, 'astropi'],
    #     ' ': ['shape 3', 50, 'pink'],
    # }

    code = {
        # letter [shape, size, colour]
        'a': pat3,
        'b': pat3,
        'c': pat2,
        'd': pat2,
        'e': pat1,
        'f': pat1,
        'g': pat4,
        'h': pat4,
        'i': pat5,
        'j': pat5,
        'k': pat6,
        'l': pat6,
        'm': pat7,
        'n': pat7,
        'o': pat8,
        'p': pat8,
        'q': pat9,
        'r': pat9,
        's': pat2,
        't': pat1,
        'u': pat9,
        'v': pat8,
        'w': pat7,
        'x': pat6,
        'y': pat5,
        'z': pat4,
        ' ': pat3,
    }

    
    #global name

    seed(5) # Generate the same random numbers each time
    no_stroke()
    draw_background()

    namel = name.lower() # Change the input to lowercase

    message = [] # Initialise the message list

    for letter in namel:
        message.append(code[letter]) # Encode each letter with a shape and add it to a list

    space = 120
    message_count = 0
    for x in range(0, 400, space):
        
        for y in range(0, 400, space):
            image(message[0], x, y, 50, 50)
            image(message[1] , x + space / 2, y + space / 2, 50, 50)  # Draw a square at the offset position
            #square(x, y, 10)  # Draw a square at (x, y)
            #square(x + space / 2, y + space / 2, 10)  # Draw a square at the offset position
            message_count =+ 1 
        message_count =+ 1 
    image(logo, 160, 160, 80, 80)
    fill(Color(0,0,0)) #black


    fill(Color(255,255,255)) #whitejade
    rect(0, 420, 400, 300)


    fill(Color(0,0,0))
    my_font = create_font("Barlow-Bold.ttf", 40)
    text_font(my_font)
    text_align('CENTER', 'CENTER')
    text(name, 200, 500)



    affl = input("Affiliation: ")
    text(affl, 200, 555)

    rect_mode(CENTER)



    filename = name +".png"
    save_canvas(filename)

def key_pressed():
    # Refresh the drawing on key press
    redraw()
    

if __name__ == '__main__':
    #print('Enter your name to make some encoded artwork:')
    #name = input()
    run(frame_rate=10)
