import discord
import os
import random, time
from utils import get_random_string

from PIL import Image, ImageDraw, ImageFont

TOKEN = 'NDQ5MDA2NDk3ODA5MDM5MzYw.DeeZfA.IJd-QYb1m3ijNSDAcxPEXmkl7-8'

client = discord.Client()
images = os.listdir('img')
bad_images = os.listdir('bad.vibes.memes')
caveras = os.listdir('blank_cavera')
saudacoes = ['fala ai meu', 'bom dia meu', 'qual foi meu', 'iae meu',
             'coe meu']
nomes = ['condecorado', 'consagrado', 'cupinxa', 'chefia', 'abençoado',
         'cacique', 'caverao', 'diabao', 'compatriota']
sounds = ['epbKsu4mh6c', 'bovKEHWI16A', 'khVOwpjo2Tc', 'g-Su7VIY_0I',
          'vNRFdQPCSAs', '2mm3nJrKcuo']
admins = ['puf3zin']



def create_meme(message, text):
    background = random.choice(caveras)
    image = Image.open('blank_cavera/' + background)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font_size = int(width/12)
    font = ImageFont.truetype('Roboto-Bold.ttf', size=font_size)
    x, y = (width/2) - len(text)*font_size/5, 200
    new_x = x - 2
    a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
    color = 'rgb(%d, %d, %d)' % (a, b, c)
    white = 'rgb(255, 255, 255)'
    draw.text((x-1, y-1), text, font=font, fill=white)
    draw.text((x+1, y-1), text, font=font, fill=white)
    draw.text((x-1, y+1), text, font=font, fill=white)
    draw.text((x+1, y+1), text, font=font, fill=white)
    draw.text((x, y), text, fill=color, font=font)
    name = get_random_string(10) + '.png'
    image.save('caveroes/' + name)
    msg = 'pega o caverao ai'
    msg += '{0.author.mention}'.format(message)
    return msg, name

def get_random_cavera(message):
    apelido = random.choice(nomes)
    saudacao = random.choice(saudacoes)
    msg = '%s %s ' % (saudacao, apelido)
    msg += '{0.author.mention}'.format(message)
    img = random.choice(images)
    return msg, img

def bad_vibes(message):
    msg = "eu ouvi bad vibes? "
    msg += '{0.author.mention}'.format(message)
    img = random.choice(bad_images)
    return msg, img


@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    content = message.content.lower()
    print (message.author)
    print (message.channel)
    author_name = str(message.author).split('#')[0]
    for nome in nomes:
        if nome in content:
            msg, img = get_random_cavera(message)
            fp = open("img/" + img, "rb")
            image = discord.File(fp)
            await message.channel.send(file=image)
            await message.channel.send(msg)
            break
    if 'bad' in content:
        msg, img = bad_vibes(message)
        fp = open("bad.vibes.memes/" + img, "rb")
        image = discord.File(fp)
        await message.channel.send(file=image)
        await message.channel.send(msg)

    if content.startswith('cria'):
        msg, img = create_meme(message, content[5:])
        fp = open("caveroes/" + img, "rb")
        image = discord.File(fp)
        await message.channel.send(file=image)
        await message.channel.send(msg)

    if 'com covid' in content:
        msg = random.choice(['ta corongado', 'ta sim', 'aham', 'pegou mas ja passou', 'ta safe'])
        await message.channel.send(msg)
        
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)