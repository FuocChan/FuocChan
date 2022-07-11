def dfs(u):
    loc=[]
    DinhKe=[]
    for i in A:
        if u in i:
            i.remove(u)
            loc.append(i)
    if len(loc)>0:
        for i in loc:
            if i != []:
                DinhKe.append(i[0])
    visited[u-1]='T'
    xuat.append(u)
    if len(DinhKe)>0:
        for v in DinhKe:
            if visited[v-1]=='F':
                dfs(v)

aV,aE=int(input()),int(input())
A=[]
visited=['F']*aV
cnt=0

for i in range(0,aE):
    x,y=int(input()),int(input())
    A.append([x,y])
for i in range(1,aV+1):
    xuat=[]
    if visited[i-1]=='F':
        cnt+=1
        dfs(i)
        print(xuat)
print('số liên thông:', cnt)

'''
intput
10
8
1
2
2
3
2
4
3
6
3
7
6
7
5
8
8
9
'''