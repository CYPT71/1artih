import string, unicodedata, re
from textwrap import wrap
regex = re.compile("[^A-Za-z]+")
def remove_transform(text):
    # replace accentuted word
    text = unicodedata.normalize("NFKD", text).encode("ASCII", "ignore").decode("utf8")
    # return only letter in lower case
    return re.sub(regex, '', text).lower().replace("w", "")


def make_square(key):
    # ord and extract letters
    key = remove_transform(key)

    letters = (letter_key := sorted(set(key),key=key.index)) + [l for l in string.ascii_lowercase if l not in letter_key and l != "w"]

    print([letters[i:i+5] for i in range(0, len(letters), 5)])
    return [letters[i:i+5] for i in range(0, len(letters), 5)]

def cutter(text, n):
   return " ".join(wrap(remove_transform(text), n))
