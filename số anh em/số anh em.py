def soanhem(x,y): # kiểm tra số anh em
    tong1 = 0
    tong2 = 0
    if x > 1 and y > 1: # 1 ko phải snt
        if x != y: # ko trùng nhau
            for i in range(2,x):
                if x % i == 0:
                    tong1 += i # tổng ước x(ở đây là a)
            for i in range(2, y):
                if y % i == 0:
                    tong2 += i # tổng ước y(ở đấy là b)
            if tong1 != 0 and tong2 != 0: # khác -
                if tong1 == tong2:
                    if x not in lst and y not in lst: #để tránh x, y lập lại 
                        lst.append(x)
                        lst.append(y)
                        print(x, '-', y)    
def check(a):
    for b in range(2,n+1): # cho chạy từ 2-n
        soanhem(a,b) #kiemtra a(là m) với các số từ 2->n

lst = []
n = int(input()) #nhập n
for m in range(2,n+1): # chạy từ 2-n (1 ko phải snt)
    check(m) # kiểm tra từ 2->n 
