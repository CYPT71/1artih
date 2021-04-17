def FoundLetters(a, b, square):
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
    text = [e for e in text if e != ""]
    lastElem = text[-1]
    text = text[:-1]
    result= ""
    for i in range(0, len(text), 2):
        for j in range(0, len(text[i])):
            try:
                result += FoundLetters(text[i][j],text[i+1][j], square)
            except:
                break
    
    print(result)

    return result