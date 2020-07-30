import os, random, sys
from PIL import Image, ImageDraw, ImageFont

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

def draw_border (draw, text, font, color, x, y):
    draw.text((x-1, y-1), text, font=font, fill=color)
    draw.text((x+1, y-1), text, font=font, fill=color)
    draw.text((x-1, y+1), text, font=font, fill=color)
    draw.text((x+1, y+1), text, font=font, fill=color)

def split_message(text):
    lista = text.split(' ')
    count = 0
    lines = []
    tmp = ['a','b']
    for word in lista:
        tmp[count] = word
        count += 1
        if count == 2:
            lines.append(" ".join(tmp))
            count = 0
    lines.append(" ".join(tmp[:count]))
    return lines

def create_meme(text):
    image = Image.open('blank_cavera/70.png')
    draw = ImageDraw.Draw(image)
    width, height = image.size
    font_size = int(width/10)
    x, y = (width/2), 200
    white = 'rgb(255, 255, 255)'
    texts = split_message(text)
    for line in texts:
        font_name = random.choice(fonts)
        print(font_name)
        font = ImageFont.truetype(font_name, size=font_size + random.randint(-20, 20))
        a, b, c = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
        color = 'rgb(%d, %d, %d)' % (a, b, c)
        diff = len(line)*font_size/4 + random.randint(-100, 100)
        draw_border(draw, line, font, white, x-diff, y)
        draw.text((x-diff, y), line, fill=color, font=font)
        y += 60
    image.save('teste.png')

create_meme('caveirao loko testando testando')