import discord
import os
import random, time
from utils import get_random_string, split_message, load_token
from PIL import Image, ImageDraw, ImageFont

TOKEN = ''
client = discord.Client()
images = os.listdir('img')

fonts = ['arial.ttf', 'arialbd.ttf', 'arialbi.ttf', 'ariali.ttf', 'ariblk.ttf', 'Awesome Season Personal Use.ttf', 'bahnschrift.ttf',
         'Bebas-Regular.ttf', 'Bubblegum.ttf', 'built titling bd it.ttf', 'built titling bd.ttf', 'built titling el it.ttf', 'built titling el.ttf',
         'built titling lt it.ttf', 'built titling lt.ttf', 'built titling rg it.ttf', 'built titling rg.ttf', 'built titling sb it.ttf',
         'built titling sb.ttf', 'calibri.ttf', 'calibrib.ttf', 'calibrii.ttf', 'calibril.ttf', 'calibrili.ttf', 'calibriz.ttf', 'cambriab.ttf',
         'cambriai.ttf', 'cambriaz.ttf', 'Candara.ttf', 'Candarab.ttf', 'Candarai.ttf', 'Candaral.ttf', 'Candarali.ttf', 'Candaraz.ttf',
         'CaviarDreams.ttf', 'CaviarDreams_Bold.ttf', 'CaviarDreams_BoldItalic.ttf', 'CaviarDreams_Italic.ttf', 'comic.ttf', 'comicbd.ttf',
         'comici.ttf', 'comicz.ttf', 'consola.ttf', 'consolab.ttf', 'consolai.ttf', 'consolaz.ttf', 'constan.ttf', 'constanb.ttf', 'constani.ttf',
         'constanz.ttf', 'corbel.ttf', 'corbelb.ttf', 'corbeli.ttf', 'corbell.ttf', 'corbelli.ttf', 'corbelz.ttf', 'cour.ttf', 'courbd.ttf', 'courbi.ttf',
         'couri.ttf', 'Courier Final Draft Bold.ttf', 'Courier Final Draft Italic.ttf', 'Courier Final Draft Regular.ttf', 'ebrima.ttf', 'ebrimabd.ttf',
         'Excalibur Nouveau.ttf', 'framd.ttf', 'framdit.ttf', 'Gabriola.ttf', 'gadugi.ttf', 'gadugib.ttf', 'georgia.ttf', 'georgiab.ttf', 'georgiai.ttf',
         'georgiaz.ttf', 'Helvetica-Bold.ttf', 'Helvetica-BoldOblique.ttf', 'Helvetica-Light.ttf', 'Helvetica-LightOblique.ttf', 'Helvetica-Oblique.ttf',
         'Helvetica.ttf', 'himalaya.ttf', 'holomdl2.ttf', 'impact.ttf', 'Inkfree.ttf', 'javatext.ttf', 'JMH Typewriter.ttf', 'Kiona-Itallic.ttf', 'Kiona-Regular.ttf',
         'LeelaUIb.ttf', 'LeelawUI.ttf', 'LeelUIsl.ttf', 'lucon.ttf', 'l_10646.ttf', 'malgun.ttf', 'malgunbd.ttf', 'malgunsl.ttf', 'marlett.ttf', 'micross.ttf',
         'mixolydian titling bd it.ttf', 'mixolydian titling bd.ttf', 'mixolydian titling bk it.ttf', 'mixolydian titling bk.ttf', 'mixolydian titling el it.ttf',
         'mixolydian titling el.ttf', 'mixolydian titling lt it.ttf', 'mixolydian titling lt.ttf', 'mixolydian titling rg it.ttf', 'mixolydian titling rg.ttf',
         'mixolydian titling ul it.ttf', 'mixolydian titling ul.ttf', 'mmrtext.ttf', 'mmrtextb.ttf', 'monbaiti.ttf', 'MonospaceTypewriter.ttf', 'msyi.ttf', 'mvboli.ttf',
         'Nirmala.ttf', 'NirmalaB.ttf', 'NirmalaS.ttf', 'ntailu.ttf', 'ntailub.ttf', 'OptimusPrinceps.ttf', 'OptimusPrincepsSemiBold.ttf', 'pala.ttf', 'palab.ttf',
         'palabi.ttf', 'palai.ttf', 'phagspa.ttf', 'phagspab.ttf', 'Quiche.ttf', 'Roboto-Black.ttf', 'Roboto-BlackItalic.ttf', 'Roboto-Bold.ttf', 'Roboto-BoldCondensed.ttf',
         'Roboto-BoldCondensedItalic.ttf', 'Roboto-BoldItalic.ttf', 'Roboto-Condensed.ttf', 'Roboto-CondensedItalic.ttf', 'Roboto-Italic.ttf', 'Roboto-Light.ttf',
         'Roboto-LightItalic.ttf', 'Roboto-Medium.ttf', 'Roboto-MediumItalic.ttf', 'Roboto-Regular.ttf', 'Roboto-Thin.ttf', 'Roboto-ThinItalic.ttf', 'segmdl2.ttf',
         'segoepr.ttf', 'segoeprb.ttf', 'segoesc.ttf', 'segoescb.ttf', 'segoeui.ttf', 'segoeuib.ttf', 'segoeuii.ttf', 'segoeuil.ttf', 'segoeuisl.ttf', 'segoeuiz.ttf',
         'seguibl.ttf', 'seguibli.ttf', 'seguiemj.ttf', 'seguihis.ttf', 'seguili.ttf', 'seguisb.ttf', 'seguisbi.ttf', 'seguisli.ttf', 'seguisym.ttf', 'simsunb.ttf',
         'SourceCodePro-Black.ttf', 'SourceCodePro-Bold.ttf', 'SourceCodePro-ExtraLight.ttf', 'SourceCodePro-Light.ttf', 'SourceCodePro-Medium.ttf', 'SourceCodePro-Regular.ttf',
         'SourceCodePro-SemiBold.ttf', 'Square.ttf', 'Swkeys1.ttf', 'sylfaen.ttf', 'symbol.ttf', 'tahoma.ttf', 'tahomabd.ttf', 'taile.ttf', 'taileb.ttf', 'theboldfont.ttf',
         'times.ttf', 'timesbd.ttf', 'timesbi.ttf', 'timesi.ttf', 'trebuc.ttf', 'trebucbd.ttf', 'trebucbi.ttf', 'trebucit.ttf', 'verdana.ttf', 'verdanab.ttf', 'verdanai.ttf',
         'verdanaz.ttf', 'Wallman-Bold-free.ttf']

bad_images = os.listdir('bad.vibes.memes')
caveras = os.listdir('blank_cavera')
saudacoes = ['fala ai meu', 'bom dia meu', 'qual foi meu', 'iae meu',
             'coe meu']
nomes = ['condecorado', 'consagrado', 'cupinxa', 'chefia', 'abençoado',
         'cacique', 'caverao', 'diabao', 'compatriota']
sounds = ['epbKsu4mh6c', 'bovKEHWI16A', 'khVOwpjo2Tc', 'g-Su7VIY_0I',
          'vNRFdQPCSAs', '2mm3nJrKcuo']
admins = ['puf3zin']
banned_list = []

def draw_border (draw, text, font, color, x, y):
    draw.text((x-1, y-1), text, font=font, fill=color)
    draw.text((x+1, y-1), text, font=font, fill=color)
    draw.text((x-1, y+1), text, font=font, fill=color)
    draw.text((x+1, y+1), text, font=font, fill=color)


def create_meme(message, text, ban):
    print (ban)
    if ban:
        text = 'nao introsa vc ta banido parça'
    background = random.choice(caveras)
    image = Image.open('blank_cavera/' + background)
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font_size = int(width/10)
    #print(font_name)
    x, y = (width/2), 200
    white = 'rgb(255, 255, 255)'
    print (text)
    texts = split_message(text)
    for line in texts:
        font_name = random.choice(fonts)
        font = ImageFont.truetype(font_name, size=font_size + random.randint(-20, 20))
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        color = 'rgb(%d, %d, %d)' % (a, b, c)
        diff = len(line)*font_size/4 + random.randint(-100, 100)
        draw_border(draw, line, font, white, x-diff, y)
        draw.text((x-diff, y), line, fill=color, font=font)
        y += 60
    name = get_random_string(10) + '.png'
    image.save('caveroes/' + name)
    return name

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
    try:
        if message.author == client.user:
            return
        content = message.content
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
            
        if 'bad' in content.lower():
            msg, img = bad_vibes(message)
            fp = open("bad.vibes.memes/" + img, "rb")
            image = discord.File(fp)
            await message.channel.send(file=image)
            await message.channel.send(msg)

        if 'com covid' in content.lower():
            msg = random.choice(['ta corongado', 'ta sim', 'aham', 'pegou mas ja passou', 'ta safe'])
            await message.channel.send(msg)

        if content.startswith('.cria '):
            print(message.author)
            ban = False
            if author_name in banned_list:
                ban = True
            img = create_meme(message, content[6:], ban)
            fp = open("caveroes/" + img, "rb")
            image = discord.File(fp)
            await message.channel.send(file=image)
            await message.delete()
    except discord.errors.Forbidden:
        print ("forbidden")


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


def main():
    if TOKEN == '':
        TOKEN = load_token()
    client.run(TOKEN)

if __name__ == "__main__":
    main()