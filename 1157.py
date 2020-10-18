import sys

count = [0] * 26
line = sys.stdin.readline()
for i in line[:-1]:
    if i.islower():
        count[ord(i) - 97] += 1
    else:
        count[ord(i) - 65] += 1
largest = max(count)
if count.count(largest) != 1:
    print("?")
else:
    print(chr(count.index(largest) + 65))