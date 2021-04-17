import string

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

cutter=lambda text,n:' '.join((text:=text.replace(" ","").replace("\n","").lower())[i:i+n]for i in range(0,len(text),n))


