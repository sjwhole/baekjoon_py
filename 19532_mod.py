import sys
from sympy import Symbol, solve

x = Symbol('x')
y = Symbol('y')

a, b, c, d, e, f = map(int, sys.stdin.readline().split())
equation1 = a * x + b * y - c
equation2 = d * x + e * y - f
sol = solve((equation1, equation2))
print(sol[x], sol[y])
