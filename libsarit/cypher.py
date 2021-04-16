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
    mainStr += (x + y)

    return mainStr

