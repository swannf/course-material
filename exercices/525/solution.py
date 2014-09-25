def collatz(start):
    n = start
    chain = 1
    while n != 1:
        if n % 2 == 0:
            n = n / 2
            chain += 1
        else:
            n = 3*n + 1
            chain += 1
    return(chain)


final = 0
for i in range(837799, 837800):
    res = collatz(i)
    final = max(final, res)
    if max(final, res) == res:
        starting = i
print(starting)
