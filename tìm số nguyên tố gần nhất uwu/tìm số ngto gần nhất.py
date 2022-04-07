n = int(input())
# ktra số nguyên tố
def snt(x):
    check = 0
    for i in range(2,x):
        if x%i==0:
            check+=1
    if check == 0:
        print(x)
snt(n)
# số nguyên tố lớn hơn N
def sntbigger(x):
    check = 0
    for i in range(2,x):
        if x%i==0:
            check+=1
    if check != 0:
        sntbigger(x+1)
    else:
        print(x)
sntbigger(n+1)
# số nguyên tố nhỏ hơn N
def sntsmaller(x):
    check = 0
    for i in range(2,x):
        if x%i==0:
            check+=1
    if check != 0:
        sntsmaller(x-1)
    else:
        print(x)
sntsmaller(n-1)

