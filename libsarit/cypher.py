from .functionalPart import foundCorrespondencies
def cypher(text, square):
    x = ""
    y = ""
    mainStr = ""
    
    for letter in text:
        if letter == " ":
            print(x, y)
            mainStr += (x +" "+ y+" ")            
            x = ""
            y = ""
        else:
            a, b = foundCorrespondencies(letter, square)
            
            x += a
            y += b
    mainStr += (x +" "+ y+" ")

    return mainStr

