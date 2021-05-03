def encryption(letter, square):
    
    return ("", "") if len(square) < 1 or len(square[0])<1 else [part for sub in square for i, l in enumerate(sub) if l ==letter for part in (sub[0], square[-1][i])]
    

def cypher(text, square):
    x, y, mainStr = "", "", ""
    for letter in text.replace("w", "vv"):
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

