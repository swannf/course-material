def is_prime(num):
    div = []
    if num <= 1:
        return(False)
    else:
        for i in range(2, int((num ** 0.5)+1)):
            if num % i == 0:
                div.append(i)
                break
        if len(div) == 0:
            return(True)
        else:
            return(False)
