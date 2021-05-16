def encryption(letter, square): 
    i = -1
    while (i:=i+1) < len(square): 
        if letter in (sub := square[i]): return (sub[0], square[-1][sub.index(letter)])

def cypher(text, square):
    x, y, mainStr = "", "", ""
    for letter in text.replace("w", "v"):
        if letter == " ":
            mainStr += (x +" "+ y+" ")            
            x, y = "", ""
        else:
            a, b = encryption(letter, square)
            x += a
            y += b
    lastChar = x + y
    
    spacer = len(text.split(" ")[0])
    endPass = lastChar[:spacer] + " " + lastChar[spacer:]
    
    mainStr += endPass
    return mainStr

