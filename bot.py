import discord
import os
import random, time, string, math
import json
from utils import get_random_string, split_message, draw_border, filter_msg
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

client = discord.Client()

## Loading images
images = os.listdir('img')
bad_images = os.listdir('bad.vibes.memes')
caveras = os.listdir('blank_cavera')

## Loading settings
with open('settings.json') as json_file: 
    settings = json.load(json_file)

VERSAO_ATUAL = settings["VERSAO_ATUAL"]
saudacoes = settings["saudacoes"]
nomes = settings["nomes"]
bom_dias = settings["bom_dias"]
shreks = settings["shreks"]
admins = settings["admins"]
vacinados = settings["vacinados"]
banidos = settings["banidos"]
fonts = settings["fonts"]

with open('token.json') as json_file: 
    TOKEN = json.load(json_file)["TOKEN"]

## Internal lists
pessoas_com_covid = []
pessoas_sem_covid = []

def create_meme(text, ban=False):
    if ban:
        text = 'nao introsa vc ta banido parça'
    background = random.choice(caveras)
    image = Image.open('blank_cavera/' + background)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font_size = int(width/10)
    x, y = (width/2), 200
    white = 'rgb(255, 255, 255)'
    print ("\nmeme created: %s" % text)
    texts = split_message(text)
    selected_fonts = []
    for line in texts:
        font_name = random.choice(fonts)
        selected_fonts.append(font_name)
        font = ImageFont.truetype(font_name, size=font_size + random.randint(-20, 20))
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        color = 'rgb(%d, %d, %d)' % (a, b, c)
        diff = len(line)*font_size/4 + random.randint(-100, 100)
        draw_border(draw, line, font, white, x-diff, y)
        draw.text((x-diff, y), line, fill=color, font=font)
        y += 60
    name = get_random_string(10) + '.png'
    image.save('caveroes/' + name)
    print("fonts used: %s" % ", ".join(selected_fonts))
    img_file = open("caveroes/" + name, "rb")
    image = discord.File(img_file)
    return image

def get_random_cavera(message):
    apelido = random.choice(nomes)
    saudacao = random.choice(saudacoes)
    msg = '%s %s ' % (saudacao, apelido)
    msg += '{0.author.mention}'.format(message)
    img = random.choice(images)
    return msg, img

def com_covid(pessoa):
    safes = ['pegou mas ja passou', 'ta safe', 'nao', 'testou negativo parça']
    corongas = ['ta corongado', 'ta sim', 'aham', 'testou positivo kkkk se fudeu']
    jacares = ['ce ja ate vacinou, brother', 'ja tomou pikadura kkkkkkk', 'jacare nem tem covid parsa']
    if pessoa in pessoas_com_covid:
        msg = 'ja falei q sim parça, o teste não vai mudar do nada'
    elif pessoa in pessoas_sem_covid:
        msg = 'nao po, tá safe msm confia'
    elif pessoa in vacinados:
        msg = random.choice(jacares)
    else:
        flag = random.choice([0, 1])
        if flag == 1:
            msg = random.choice(corongas)
            pessoas_com_covid.append(pessoa)
        elif flag == 0:
            msg = random.choice(safes)
            pessoas_sem_covid.append(pessoa)
    return msg

def sherek():
    msg = """⢀⡴⠑⡄⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣤⣤⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠸⡇⠀⠿⡀⠀⠀⠀⣀⡴⢿⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠑⢄⣠⠾⠁⣀⣄⡈⠙⣿⣿⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⢀⡀⠁⠀⠀⠈⠙⠛⠂⠈⣿⣿⣿⣿⣿⠿⡿⢿⣆⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⢀⡾⣁⣀⠀⠴⠂⠙⣗⡀⠀⢻⣿⣿⠭⢤⣴⣦⣤⣹⠀⠀⠀⢀⢴⣶⣆
⠀⠀⢀⣾⣿⣿⣿⣷⣮⣽⣾⣿⣥⣴⣿⣿⡿⢂⠔⢚⡿⢿⣿⣦⣴⣾⠁⠸⣼⡿
⠀⢀⡞⠁⠙⠻⠿⠟⠉⠀⠛⢹⣿⣿⣿⣿⣿⣌⢤⣼⣿⣾⣿⡟⠉⠀⠀⠀⠀⠀
⠀⣾⣷⣶⠇⠀⠀⣤⣄⣀⡀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠉⠈⠉⠀⠀⢦⡈⢻⣿⣿⣿⣶⣶⣶⣶⣤⣽⡹⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠉⠲⣽⡻⢿⣿⣿⣿⣿⣿⣿⣷⣜⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣷⣶⣮⣭⣽⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣀⣀⣈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠻⠿⠿⠿⠿⠛⠉"""
    return msg

def bad_vibes(message):
    msg = "eu ouvi bad vibes? "
    msg += '{0.author.mention}'.format(message)
    img = random.choice(bad_images)
    fp = open("bad.vibes.memes/" + img, "rb")
    image = discord.File(fp)
    return msg, image
        

@client.event
async def on_message(message):
    try:
        # we do not want the bot to reply to itself
        if message.author == client.user:
            return
        content = message.content
        filtered_content = filter_msg(content)
        now_time = datetime.now().time()
        horario = now_time.strftime("%H:%M:%S")
        print ("-------------")
        print ("%s @ %s" % (message.author, message.channel))
        print ("%s: %s" % (horario, message.content))
        
        author_name, author_id = str(message.author).split('#')
        for nome in nomes:
            if nome in content:
                msg, img = get_random_cavera(message)
                fp = open("img/" + img, "rb")
                image = discord.File(fp)
                await message.channel.send(file=image)
                await message.channel.send(msg)
                break
        
        if content.startswith('.cria '):
            ban = False
            if author_name in banidos:
                ban = True
            image = create_meme(content[6:], ban)
            await message.channel.send(file=image)
            await message.delete()

        elif 'bad' in filtered_content:
            msg, image = bad_vibes(message)
            await message.channel.send(file=image)
            await message.channel.send(msg)

        elif 'com covid' in filtered_content:
            msg = com_covid(author_name)
            await message.channel.send(msg)

        else:
            for shrk in shreks:
                if shrk in content:
                    msg = sherek()
                    await message.channel.send(msg)
        
    except discord.errors.Forbidden:
        print ("forbidden")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('version %s' % VERSAO_ATUAL)

    # channels_for_bom_dia = []
    # for guild in client.guilds:
    #     for channel in guild.text_channels:
    #         if channel.name in bom_dias:
    #             channels_for_bom_dia.append(channel)

    # bom_dia_meme = create_meme("bom dia queridos, tamo online")
    # for channel in channels_for_bom_dia:
    #     await channel.send(file=bom_dia_meme)


if __name__ == "__main__":
    client.run(TOKEN)
