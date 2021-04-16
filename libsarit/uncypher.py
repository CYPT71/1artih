def FoundLetters(a, b, square):
    
    lettreX = 0
    lettreY = 0
    tmp = 0
    for e in square:
        if a in e:
            lettreX = e.index(a)
        tmp+= 1
        if b in e:
            lettreY = tmp
    print(lettreY<=len(square),  len(square[0])>=lettreX)
    return square[lettreY][lettreX]


def uncypher(text, square, n):
    text = "".join(text.split("\n"))
    textList = list(map(list, text.split(" ")))[:-1]

    print(textList)
    decodeMSG = ""
    
    print(decodeMSG)
    



    

