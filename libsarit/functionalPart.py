import string

def makeSquare(key):
    key = key.lower()
    lettersKeys = list(dict.fromkeys([k for e in key.split(" ") for k in e]))
    
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

def cutter(text, n):
    text = text.lower()
    text = list("".join(text.split(" ")))
    new_text = ""
    i = 0
    for e in text:
        if i == 7:
            new_text += " "
            i=0
        i+= 1
        new_text += e
    return new_text

