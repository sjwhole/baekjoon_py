import time

start = time.time()
count = 0
for i in range(1000000000):
    count += 1
print(time.time() - start)