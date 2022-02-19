import random
import string
from unidecode import unidecode

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

def remove_punc(msg):
    for c in msg:
        if c in string.punctuation:
            msg = msg.replace(c, "")
    return msg

def filter_msg(message):
    message = message.lower()
    message = unidecode(message)
    message = remove_punc(message)
    return message

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

def draw_border (draw, text, font, color, x, y):
    draw.text((x-1, y-1), text, font=font, fill=color)
    draw.text((x+1, y-1), text, font=font, fill=color)
    draw.text((x-1, y+1), text, font=font, fill=color)
    draw.text((x+1, y+1), text, font=font, fill=color)
    
def load_token():
    fd = open("token.key")
    key = fd.readline()
    fd.close()
    return key
