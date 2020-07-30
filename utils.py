import random
import string

def get_random_string(length):
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for i in range(length))
    return result_str

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

def load_token():
    fd = open("token.key")
    key = fd.readline()
    fd.close()
    return key