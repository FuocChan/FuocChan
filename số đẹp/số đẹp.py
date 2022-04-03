def sodep(x):
    sum = 0
    if x >= 9:
        if x == 9:
            print(x)
        else:
            for i in range(0,len(str(x))):
                sum += int(str(x)[i])
        if sum == 9:
            print(x)

n = int(input())
sodep(n)

