class Rational:
    def __init__(self, num=1, den=0):
        if den == 0:
            raise RuntimeError('Denominator can not be zero')
        div = gcd(num, den)
        self.__num = (1 if den > 0 else -1) * int(num / div)
        self.__den = int(abs(den) / div)

def gcd(n, d):
    x1 = abs(n)
    x2 = abs(d)
    gcd = 1
    c = 1
    while c <= x1 and c <= x2:
        if x1 % c == 0 and x2 % c == 0:
            gcd = c
        c += 1
    return gcd

Rational()