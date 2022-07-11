'''
intput
9
9
1
2
1
3
1
5
2
4
3
6
3
7
3
9
5
8
8
9
'''
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
xuat=[]
A=[]
visited=['F']*aV
for i in range(0,aE):
    x,y=int(input()),int(input())
    A.append([x,y])
dfs(1)
print(xuat)