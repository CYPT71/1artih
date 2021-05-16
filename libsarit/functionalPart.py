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
    key = key.lower().replace("w", "")
    letters = (lettersKeys := sorted(set(key),key=key.index)) + [l for l in string.ascii_lowercase if l not in lettersKeys and l != "w"]

    return [letters[i:i+5] for i in range(0, len(letters), 5)]


def removeTransform(text):
    # replace accentuted word
    text = unidecode.unidecode(text)
    # return only letter in lower case 
    return re.sub('[^A-Za-z]+', '', text).lower()

def cutter(text, n):
    return ' '.join((text := removeTransform(text))[i:i + n] for i in range(0, len(text), n))
