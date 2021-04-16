def FoundLetters(a, b, square):
    
    lettreX = 0
    lettreY = 0
    for x in range(0, len(square)):
        for y in range(0, len(square)):
            if square[x][y] == a:
                lettreX = x
            if square[x][y] == b:
                lettreY = y
    return square[lettreX][lettreY]


def uncypher(text, square, n):
    text = "".join(text.split("\n"))
    textList = list(map(list, text.split(" ")))[:-1]

    # print(textList)
    decodeMSG = ""
    for i in range(len(textList)//2):
        for j in range(n-1):
            decodeMSG += FoundLetters(textList[i][j], textList[i+1][j], square)
    print(decodeMSG)
    



    

