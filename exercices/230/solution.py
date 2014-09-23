import is_prime
start = 100000000
res = 0
while (res == 0):
    start += 1
    if is_prime.is_prime(start):
        res = start
print(res)
