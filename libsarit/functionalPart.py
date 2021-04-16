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
    for i in range(1, len(text)*2):
        if i%n == 0:
            text.insert(i, " ")
    
    return "".join(text)

def foundCorrespondencies(letter, square):
    tupleLetters = None
    for sub in square:
        for i, l in enumerate(sub):
            if l==letter:
                tupleLetters = (sub[0], square[-1][i])
                break
            if tupleLetters:
                break 
    return tupleLetters