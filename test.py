from libsarit import cypher, cutter, makeSquare
key = "direction academique"
text = "jumping jack flash"
n = 7
print(cypher(cutter(text, n), makeSquare(key)))
# print([foundCorrespondencies(l, makeSquare(key)) for l in cutter(text, n) if l != " "])