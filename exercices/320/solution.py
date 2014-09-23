with open('words', 'r') as f:
    alphab = 'abcdefghijklmnopqrstuvwxyz'
    dalpha = {}
    for m in alphab:
        dalpha.update({m: 0})
    res = 0
    f.readline()
    for line in f:
        res += len(line)
        counter = 0
        for l in alphab:
            dalpha[l] = dalpha[l]+line.count(l)
    for n in alphab:
        dalpha[n] = round(dalpha[n]/res, 2)
print(dalpha)
