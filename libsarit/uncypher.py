from .functionalPart import *


def uncypher(text, square):
    text = "".join(text.split("\n"))
    textList = list(map(list, text.split(" ")))
    len_sub = len(textList[0])
    pairs = []
    for i in range(len(textList)-1):
        for j in range(len_sub-1):
            pairs.append((textList[i][j],textList[i+1][j]))

    print(pairs)


