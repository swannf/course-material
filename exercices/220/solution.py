import is_prime
plist = []
for num in range(10000, 10050):
    if is_prime.is_prime(num):
        plist.append(num)
print(", ".join(map(str, plist)))
