n=int(input())

first=['2','3','5','7']
back=['1','3','7','9']

def check(num):
    for i in range(2,int(int(num)**0.5)+1):
        if int(num)%i==0:
            return
    if len(num)==n:
        print(int(num))
        return

    for b in back:
        check(num+b)

for f in first:
    check(f)
