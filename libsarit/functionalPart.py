import string

import re

try:
    import unidecode
except ImportError:
    # nif import fail we try to install the module
    import os
    import platform

    if "win" in platform.system():
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip3 install -r requirements.txt")
except OSError as e:
    print(e, "please install requirements.txt")
finally:
    import unidecode


def makeSquare(key):
    # ord and extract letters 

    lettersKeys = list(dict.fromkeys(removeTransform(key).replace("w", "v")))

    letters = lettersKeys + [l for l in string.ascii_lowercase if l not in lettersKeys and l != "w"]

    # create the square
    square = []
    sub = letters[:5]
    for l in letters:
        if len(sub) > 4:
            sub = []
            square.append(sub)

        sub.append(l)

    return square


def removeTransform(text):
    # replace accentuted word
    text = unidecode.unidecode(text)
    # return only letter in lower case 
    return re.sub('[^A-Za-z]+', '', text).lower()

def cutter(text, n):
    # transform the text 
    text = removeTransform(text)
    # return the text cutted with the right space 
    return ' '.join(text[i:i + n] for i in range(0, len(text), n))
