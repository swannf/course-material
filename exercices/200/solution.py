def is_prime(num):
    div = []
    for i in range(int((num ** 0.5)+1), 2, -1):
        if num % i == 0:
            div.append(i)
            break
    if len(div) == 0:
        return(True)
    else:
        return(False)
