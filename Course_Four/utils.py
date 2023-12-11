def gdc(x, y):
    if y == 0:
        return abs(x)
    else:
        return gdc(y, x % y)
