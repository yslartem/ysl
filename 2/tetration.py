import math
def tetration(k, n):
    if n == 0:
        return 1
    elif n == 1:
        return k
    else:
        power = tetration(k, n-1)
        return k ** power