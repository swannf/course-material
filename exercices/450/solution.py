forward = 1
backward = -1


def caesar_cypher(s, key, method):
    from string import ascii_lowercase
    letter = (ascii_lowercase)
    cript = []
    key = method*(key % 26)
    for let in s:
        if let in letter:
            cript.append(letter[abs(((letter.find(let))+key) % 26)])
        else:
            cript.append(let)
    return(''.join(cript))
