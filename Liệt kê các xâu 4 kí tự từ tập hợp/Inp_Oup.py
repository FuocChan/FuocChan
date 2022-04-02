def xuat():
    print("".join(answer[0:4]))
    dem.append(answer[0:4])
def CHL(x):
    for i in range(ord('A'),ord('F')+1):
        answer.insert(0, chr(i))
        if x == k:
            xuat()
        else:
            CHL(x+1)
      
answer = []
dem = []
k = 4
print(CHL(1))
print(len(dem))