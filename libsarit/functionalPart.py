import string

import re

try:
    import unidecode
except ImportError:
    import os
    import platform

    if "win" in platform.system():
        os.system("pip install -r requirements.txt")
    else:
        os.system("pip3 install -r requirements.txt")
except Exception as e:
    print(e, "please install requirements.txt")
finally:
    import unidecode


def makeSquare(key):
    lettersKeys = list(dict.fromkeys(removeTransform(key).replace("w", "vv")))

    letters = lettersKeys + [l for l in string.ascii_lowercase if l not in lettersKeys and l != "w"]
    square = []
    sub = letters[:5]
    for l in letters:
        if len(sub) > 4:
            sub = []
            square.append(sub)

        sub.append(l)

    return square


def removeTransform(text):
    text = unidecode.unidecode(text)
    return re.sub('[^A-Za-z]+', '', text).lower()

def cutter(text, n):
    return ' '.join((text := removeTransform(text))[i:i + n] for i in range(0, len(text), n))
