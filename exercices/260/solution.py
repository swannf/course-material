def euclidean(a, b):
    subdist = 0
    for i in range(len(a)):
        subdist += (b[i]*b[i]-a[i]*a[i])
    dist = subdist ** 0.5
    return dist


def opt_euclidean(a, b):
    import math
    subdist = 0
    for i in range(len(a)):
        subdist += math.pow(b[i], 2)-math.pow(a[i], 2)
    dist = math.sqrt(subdist)
    return dist


def np_euclidean(a, b):
    import numpy as np
    dist = np.linalg.norm(np.array(a)-np.array(b))
    return dist
