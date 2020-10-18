import sys

ham = []
drink = []
for _ in range(3):
    ham.append(int(sys.stdin.readline()))
for _ in range(2):
    drink.append(int(sys.stdin.readline()))
print(min(ham) + min(drink) - 50)