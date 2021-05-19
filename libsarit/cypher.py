def encryption(letter, square):    
    return [(line[0], square[-1][line.index(letter)]) for line in square if letter in line][0]

def cypher(text, square):
    return " ".join(" ".join(map("".join,zip(*[cypherLetter(l, square) for l in s]))) for s in text.split(" "))