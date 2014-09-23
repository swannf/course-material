F = [1, 1]
while len(F) != 10:
    F.append(F[-2]+F[-1])
print(", ".join(map(str, F)))
