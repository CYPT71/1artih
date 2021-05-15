def dencryption(a, b, square):
    a,b = a.lower(),b.lower()
    for sub in square:
        if a in sub:
            x = square.index(sub)
        if b in sub:
            y = sub.index(b)
    return square[x][y]

def uncypher(text, square):
    if isinstance(text, str): text = text.split(" ")

    if text == []: return ""

    if len(text)==1:
        t=text[0]
        text, x, y = [], t[:len(t)//2], t[len(t)//2:]
    else:
        x, y = text[0],text[1]
        for _ in range(2): text.pop(0)
    
    return "".join(dencryption(a,b, square) for a, b in zip(x,y)) + uncypher(text, square)

