#------phân tích thừa số nguyên tố-----------#
def thuasonguyento(x):
    m = n
    k = 2
    thuaso = []
    for i in range(1,m+1):
        if m % k == 0:
            m = m / k
            thuaso.append(str(int(k)))
        else:
            k = k + 1
    print(n,'=',"*".join(thuaso))
#----đếm tất cả các ước & tổng ước----------#
def demuoc(y):
    uoc = []
    for i in range(1,y+1):
        if y % i == 0:
            uoc.append(i)
    print('ước của',n,'là:',*uoc,sep=",")
    print('tổng ước của',n,'là:',sum(uoc))
       
n = int(input())
thuasonguyento(n)
demuoc(n)
