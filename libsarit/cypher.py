def encryption(letter, square):
    tupleLetters = None
    for sub in square:
        for i, l in enumerate(sub):
            
            if l==letter:
                tupleLetters = (sub[0], square[-1][i])
                break
        if tupleLetters:
            break 
    return tupleLetters

def cypher(text, square):
    text = text.lower()
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

