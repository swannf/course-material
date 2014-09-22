alpha = 'abcdefghijklmnopqrstuvwxyz'
siz = len(alpha)
for i in range(0, siz):
    for j in range(i, siz):
        if alpha[i] != alpha[j]:
            print(alpha[i]+alpha[j])