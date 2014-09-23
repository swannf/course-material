F = [1, 2]
while len(F) != 10:
    F.append(F[-2]+F[-1])
print(", ".join(map(str, F)), end='.')
