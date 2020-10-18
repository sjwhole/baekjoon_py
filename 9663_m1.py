import sys

def n_queen(sol, y):
    global count
    if len(sol) == N:
        count += 1
        return
    possible = list(range(1, N + 1))
    for i in range(len(sol)):
        possible.remove(sol[i])
        d = len(sol) - i
        if sol[i] + d in possible:
            possible.remove(sol[i] + d)
        if sol[i] - d in possible:
            possible.remove(sol[i] - d)
    if possible:
        for num in possible:
            sol.append(num)
            n_queen()








N = int(sys.stdin.readline())
count = 0
sol = []