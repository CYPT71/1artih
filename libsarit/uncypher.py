def unencryption(a, b, square):
    a, b, index = a.lower(), b.lower(), 0
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
    result = ""
    for i in range(0, len(text) - 2, 2):
        for j in range(0, len(text[i])):
            result += unencryption(text[i][j], text[i + 1][j], square)

    last = text[-2] + text[-1]
    last = [last[:len(last) // 2], last[len(last) // 2:]]

    for i in range(len(last[0])):
        result += unencryption(last[0][i], last[1][i], square)

    return result
