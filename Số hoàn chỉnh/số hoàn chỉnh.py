def sohoanching(x):
    lst = []
    for i in range(1,x):
        if x % i == 0:
            lst.append(i)
    if sum(lst) == x:
        print(x)

n = int(input())
for i in range(1,n+1):
    sohoanching(i)

