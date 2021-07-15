import math


def quadratic(a, b, c):
    if not isinstance(a, (float, int)):
        raise TypeError('bad operand type')
    if not isinstance(b, (float, int)):
        raise TypeError('bad operand type')
    if not isinstance(c, (float, int)):
        raise TypeError('bad operand type')
    r = b * b - 4 * a * c
    if r < 0 :
        raise TypeError('无解！')
    x1 = (-b + math.sqrt(r)) / (2 * a)
    x2 = (-b - math.sqrt(r)) / (2 * a)
    return x1, x2


print('quadratic(2,3,1) = ', quadratic(2, 3, 1))
