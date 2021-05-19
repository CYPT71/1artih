import string, re, unicodedata
from textwrap import wrap

def removeTransform(text):
    # replace accentuted word
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf8")
    # return only letter in lower case 
    return re.sub('[^A-Za-z]+', '', text).lower().replace("w", "v")


def makeSquare(key):
    # ord and extract letters 
    key = removeTransform(key)
    letters = (lettersKeys := sorted(set(key),key=key.index)) +\
                [l for l in string.ascii_lowercase if l not in lettersKeys and l != "w"]

    return [letters[i:i+5] for i in range(0, len(letters), 5)]

def cutter(text, n):
   return " ".join(wrap(removeTransform(text), n))
