import is_prime
res = 0
for num in range(2, 1001):
    if is_prime.is_prime(num):
        res += num
print(res)
