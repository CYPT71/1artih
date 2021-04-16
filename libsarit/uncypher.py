def FoundLetters(a, b, square):
    a = a.lower()
    b = b.lower()
    index = []
    for columns, rows in enumerate(square):
        if b in rows:
            index.append(rows.index(b))
        if a in rows:
            index.append(columns)
    print(index)
    return square[index[0]] [index[1]] 

def get_paires(text):
    text = text.replace("\n", "").split(" ")
    pairs = []

    for i in range(len(text)//2):
        for j in range(len(text[i])):
            pairs.append((text[i][j], text[i+1][j]))

        i+=1     
    

    return pairs     

def replaceElement(old, new, l):
    return [(e, new)[e==old] for e in l]    

def uncypher(text, square, n):
    
    paires = get_paires(text)

    result = ""
    i = 0
    for paire in paires:
        print(FoundLetters(paire[0], paire[1], square), paire)
        result += FoundLetters(paire[0], paire[1], square)
        
        if i == 10:
            break
        i+= 1
    
    return result
        









    

    


    



    

