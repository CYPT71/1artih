
def dencryption(a, b, square):
    a,b, index = a.lower(),b.lower(), 0
    Letterline = []
    for line in square:
        if a in line:
            Letterline = line
        if b in line:
            index = line.index(b)
    return Letterline[index]

def uncypher(text, square):
    text = text.split(" ")
    result = ""
    last = text[-2]+text[-1]
    text.remove(text[-2])
    text.remove(text[-1])
    
    for i in range(0, len(text)-2, 2):

        for a, b in zip(text[i], text[i+1]):
            result += dencryption(a, b, square)
    
    print(last)
    for a, b in zip():
        result += dencryption(a, b, square)
    print(result)
    return ""
