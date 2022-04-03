def songuyento(x): # ktra số ngto
    dem = 0
    if x != 1:
        for j in range(2,x):
            if x % j == 0:
                dem += 1
        if dem == 0:
            answer.append(str(x))

with open('input.txt', 'r') as FileInp: # lấy dữ liệu từ inp
    m =  FileInp.readline().rstrip('\n')
    n =  FileInp.readline().rstrip('\n')
answer = []
for i in range(int(m),int(n)):
    songuyento(i)

FileOut = open('output', 'w') # xuất file
FileOut.write(", ".join(answer))

