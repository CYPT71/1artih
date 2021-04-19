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
    print(e)
finally:
    import unidecode
    
def makeSquare(key):
    key = key.lower()
    lettersKeys = list(dict.fromkeys(key.replace(" ", "")))
    
    rest = [l for l in string.ascii_lowercase if l not in lettersKeys and l!='w']
    letters = lettersKeys+rest
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
    return re.sub('[^A-Za-z]+', '', text)



cutter=lambda text,n:' '.join((text:=removeTransform(text))[i:i+n]for i in range(0,len(text),n))


