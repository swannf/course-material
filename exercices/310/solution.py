with open('words', 'r') as f:
    f.readline()
    res = 0
    for line in f:
        res += line.count('e')
print(res)
