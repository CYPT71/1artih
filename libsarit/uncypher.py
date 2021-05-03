
def unencryption(a, b, square):
    a,b, index = a.lower(),b.lower(), 0
    Letterline = []
    for line in square:
        if a in line:
            Letterline = line
        if b in line:
            index = line.index(b)
    return Letterline[index]
    
def uncypher(text, square):
    text = text.split(" ")
    text = [e for e in text if e != ""]
    result= ""
    spacer = len(text[0])
    end=2
    if list(map(len, text))[-2] == spacer:
        end=1   
    for i in range(0,len(text)-end,2):
        for j in range(0, spacer):
                
            result += unencryption(text[i][j],text[i+1][j], square)
    
    last = text[-1]
    if end == 2:
        last = text[-2] + text[-1]
    
    lenLast = len(last)//2
    last = [last[:lenLast],last[lenLast:]]

    

    for i in range(lenLast):
        result += unencryption(last[0][i], last[1][i], square)

    return result