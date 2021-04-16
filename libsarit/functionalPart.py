import string

def makeSquare(key):
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
    text = list("".join(text.split(" ")))
    j = 0
    for i in range(0, len(text)*2-1):
        j+= 1
        if j-1 == 7:
            text.insert(i, " ")
            j=0
    print(text)
    return "".join(text)

