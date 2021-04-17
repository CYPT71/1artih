def FoundLetters(a, b, square):
    a = a.lower()
    b = b.lower()
    indexA = None
    indexB = None
    i = 0
    while indexA is None or indexB is None:
        if a in square[i]:
            indexA = i
        if b in square[i]:
            indexB = square[i].index(b)
        i += 1
    #print(indexA, indexB)
    return square [indexA][indexB]


def get_paires(text):
    text = text.replace("\n", "").split(" ")
    pairs = []

    for i in range(len(text)//2+1):
        for j in range(len(text[i])):
            pairs.append((text[i][j], text[i+1][j]))
        i+=1     
    return pairs     
  

def uncypher(text, square):
    
    paires = get_paires(text)

    result = ""
    i = 0
    for paire in paires:
        print(FoundLetters(paire[0], paire[1], square), paire)
        result += FoundLetters(paire[0], paire[1], square)
        
        if i == 20:
            break
        i+= 1
    
    return result
        









    

    


    



    

