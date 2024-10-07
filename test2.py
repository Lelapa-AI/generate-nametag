from PIL import Image, ImageDraw, ImageFont
from random import randint, seed
s = 50
logo = Image.open('logo.png').resize((s, s))
pat1 = Image.open('pat1.png').resize((s, s))
pat2 = Image.open('pat2.png').resize((s, s))
pat3 = Image.open('pat3.png').resize((s, s))
pat4 = Image.open('pat4.png').resize((s, s))
pat5 = Image.open('pat5.png').resize((s, s))
pat6 = Image.open('pat6.png').resize((s, s))
pat7 = Image.open('pat7.png').resize((s, s))
pat8 = Image.open('pat8.png').resize((s, s))
pat9 = Image.open('pat9.png').resize((s, s))

# Adds a background colour
def draw_background(draw):
    draw.rectangle([0, 0, 400, 666], fill=(0, 0, 0))

def draw_namecard(name, affl):

    code = {
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

    seed(5)
    img = Image.new('RGB', (400, 666), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    draw_background(draw)

    namel = name.lower()
    message = [code[letter] for letter in namel]
    space = 120
    message_count = 0
    for x in range(0, 400, space):
        for y in range(0, 400, space):
            img.paste(message[0], (x, y))
            img.paste(message[1], (x + space // 2, y + space // 2))
            message_count += 1
        message_count += 1

    img.paste(logo.resize((80,80)), (160, 160))

    draw.rectangle([0, 420, 400, 420+300], fill=(255, 255, 255))

    font = ImageFont.truetype("Barlow-Bold.ttf", 40)
    draw.text((200, 500), name, fill=(0, 0, 0), font=font, anchor='mm')
    draw.text((200, 555), affl, fill=(0, 0, 0), font=font, anchor='mm')

    filename = name + ".png"
    img.save(filename)
    
def main():
    name = input("Enter a name: ")
    affl = input("Affiliation: ")
    draw_namecard(name, affl)

if __name__ == '__main__':
    main()