def xuat():
    print(*answer[0:3],sep="")
def LietKe(x):
    for i in range(0, 2):
        answer.insert(0, i)
        if x == 3:
            xuat()
        else:
            LietKe(x+1)

answer = []
print(LietKe(1))

