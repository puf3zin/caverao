import os, random, sys
from PIL import Image, ImageDraw, ImageFont

def create_meme(text):
    image = Image.open('caveirao.png')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font_size = int(width/12)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=font_size)
    x, y = (width/2) - len(text)*font_size/5, 200
    a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = 'rgb(%d, %d, %d)' % (a, b, c)
    white = 'rgb(255, 255, 255)'
    draw.text((x-1, y-1), text, font=font, fill=white)
    draw.text((x+1, y-1), text, font=font, fill=white)
    draw.text((x-1, y+1), text, font=font, fill=white)
    draw.text((x+1, y+1), text, font=font, fill=white)
    draw.text((x, y), text, fill=color, font=font)
    image.save('teste.png')

create_meme(sys.argv[1])