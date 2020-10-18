n=[]
l=int(input())
for _ in range(l):
    n.append(int(input()))
for i in range(1,l//2+1):
    print(n.index(i))
    n.remove(i)
    print(l-n.index(l-i+1)-(2*i-1)-1)
    n.remove(l-i+1)
if l%2!=0:
    print(0)