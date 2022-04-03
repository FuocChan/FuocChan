def xuat():
    print(*answer[0:n],sep="")
def chinhhoplap(x):
    for i in range(0, n+1):
        answer.insert(0, i)
        if x == n:
            xuat()
        else:
            chinhhoplap(x+1)

n = 4
answer = []
print(chinhhoplap(1))