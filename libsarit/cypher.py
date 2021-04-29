def encryption(letter, square):
    
    return ("", "") if len(square) < 1 or len(square[0])<1 else [part for sub in test for i, l in enumerate(sub) if l ==letter for part in (sub[0], test[-1][i])]
    

def cypher(text, square):
    text = text.replace("w", "vv")
    x = ""
    y = ""
    mainStr = ""
    for letter in text:
        if letter == " ":
            mainStr += (x +" "+ y+" ")            
            x = ""
            y = ""
        else:
            a, b = encryption(letter, square)
            
            x += a
            y += b
    lastChar = x + y
    spacer = len(text.split(" ")[0])
    endPass = lastChar[:spacer] + " " + lastChar[spacer:]
    
    mainStr += endPass

    return mainStr

