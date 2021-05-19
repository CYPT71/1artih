def encryption(letter, square): 
    
    for line in square: 
        if letter in line: return (line[0], square[-1][line.index(letter)])

def cypher(text, square):
    x, y, mainStr = "", "", ""
    for letter in text:
        if letter == " ":
            mainStr += (x +" "+ y+" ")            
            x, y = "", ""
        else:
            a, b = encryption(letter, square)
            x += a
            y += b
    lastChar = x + y
    
    spacer = len(text.split(" ", 1)[0])
    
    return mainStr + lastChar[:spacer] + " " + lastChar[spacer:]
