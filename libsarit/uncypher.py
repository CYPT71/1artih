def decryption(a, b, square):
   for line in square:
        if a.lower() in line : 
            if b not in square[-1]:
    
                raise Exception("La clef a été changé")

            return line[square[-1].index(b.lower())]

def uncypher(text, square):
    if isinstance(text, str): text = text.split(" ")
    if text == []: return ""
    
    if len(text)==1:
        t=  text[0]
        text, x, y = [], t[:len(t)//2], t[len(t)//2:]
    else:
        if len(text[0]) != len(text[1]):
            t= "".join(text)
            text, x, y = [], t[:len(t)//2], t[len(t)//2:]
        else:
            x, y = text[0],text[1]
            for _ in range(2): text.pop(0)
    try:
        return "".join(decryption(a,b, square) for a, b in zip(x,y)) + uncypher(text, square)
    except Exception as e:
        print(e)

        return ' '
