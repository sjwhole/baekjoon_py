T = int(input())

info = []
for i in range(T):
    info.append(input())

info.sort(key=lambda x: int(x[:x.index(" ")]))

for id in info:
    print(id)