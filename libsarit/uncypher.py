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
    text, result = text.split(" "), ""
    for i in range(0, len(text)//2+1, 2):
        for j in range(len(text[i])):
            # print(text[i][j],text[i+1][j], FoundLetters(text[i][j],text[i+1][j], square))
            result += FoundLetters(text[i][j],text[i+1][j], square)
        
    return result