def euclidean(a, b):
    subdist = 0
    for i in range(len(a)):
        subdist += ((a[i]-b[i])*(a[i]-b[i]))
    dist = subdist ** 0.5
    return dist


def opt_euclidean(a, b):
    import math
    subdist = 0
    for i in range(len(a)):
        subdist += math.pow(a[i]-b[i], 2)
    dist = math.sqrt(subdist)
    return dist


def np_euclidean(a, b):
    import numpy as np
    dist = np.linalg.norm(np.array(a)-np.array(b))
    return dist


def benchmark(funcs, a, b):
    import timeit
    time = timeit.timeit(funcs[1](a, b), 10)
    return(time)
