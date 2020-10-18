import sys

string = sys.stdin.readline()
jo = 0
io = 0
for i in range(len(string) - 2):
    temp = string[i: i + 3]
    if temp == "JOI":
        jo += 1
    if temp == "IOI":
        io += 1

print(jo)
print(io)