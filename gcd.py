def gcd(x, y):
    if x < y:
        x, y = y, x
    while x % y != 0:
        y = x % y
    return y


def lcm(x, y):
    if x < y:
        x, y = y, x
    return x * y // gcd(x, y)


print(gcd(1071, 1029))
print(lcm(1029, 1071))
