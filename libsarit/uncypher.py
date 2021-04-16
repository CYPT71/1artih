from .functionalPart import *


def FoundLetters(a, b, square):
    line = None
    index = None
    for l in square:
        if a in l:
            line = l.copy()
            break
    print(line)
    for e in square:
        if b in e:
            index = e.index(b)
    return line[index]


def uncypher(text, square):
    text = "".join(text.split("\n"))
    textList = list(map(list, text.split(" ")))
    len_sub = len(textList[0])
    pairs = []
    for i in range(len(textList)//2):
        for j in range(len_sub-1):
            pairs.append((textList[i][j],textList[i+1][j]))
        


    print(pairs)


