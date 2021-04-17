def FoundLetters(a, b, square):
    a = a.lower()
    b = b.lower()
    Letterline = []
    index = 0
    for line in square:
        if a in line:
            Letterline = line
        if b in line:
            index = line.index(b)
    return Letterline[index]
    


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
    s_count = 0
    for paire in paires:
        if s_count == 7:
            result += " "
            s_count = 0
        result += FoundLetters(paire[0], paire[1], square) 
        
        
        i+= 1
        s_count += 1
    clear = ""
    for i in result.split(" "):
        if len(i.replace("s", ""))> 0:
            clear += i
    return clear
        









    

    


    



    

