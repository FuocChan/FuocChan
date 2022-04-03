def check(x):
    dem = 0
    sum = 0
    for i in range(2,x): #kiemtralan1
        if x % i == 0:
            dem += 1
    if dem == 0: #songuyento
        dem = 0 # reset dem
        for i in range(0,(len(str(x)))):
            sum += int(str(x)[i]) # tổng các kí tự
        for i in range(2,sum): #kimtralan2
            if sum % i == 0:
                dem += 1
        if dem == 0:
            dem = 0
            sum = 0
            print(x)

n = int(input()) # nhập n
startlst = ['1'] # điểm bắt đầu
endlst = [] # điểm kết thúc

for i in range(1,n): #1n
    startlst.append('0')
for i in range(1,n+1):
    endlst.append('9') #9n

for a in range(int("".join(startlst)),int("".join(endlst))+1): #start -> end
    check(a)
    