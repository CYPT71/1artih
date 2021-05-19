def encryption(letter, square): 
    
    for line in square: 
        if letter in line: return (line[0], square[-1][line.index(letter)])

def cypher():
    return " ".join(" ".join(map("".join,zip(*[cypherLetter(l, square) for l in s]))) for s in text.split(" "))