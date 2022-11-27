def dfs(x,y,n):
    global depth,visitado,chegada
    if x == y:
        chegadadfs.append(n)
    for node in ladj[x]:
        if tempo[node[0]] > n:
            tempo[node[0]] = n
            depth.append((node,n))
    if not depth:return
    new = depth.popleft()
    dfs(new[0][0],y,new[1]+new[0][1])

def gfs(x,y,caminho,t,p):
    # print(caminho)
    global depth,chegada,v
    if x == y:
        chegadagfs.append(t)
        # print(t)
        return
    for node in ladj[x]:
        x1 = node[0]
        t1 = node[1]
        p1 = node[2]
        if x1 not in caminho and p + p1 <= v:
            gfs(x1,y,caminho+[x1],t + t1,p+p1)
import sys
sys.setrecursionlimit(10000000)
from collections import deque
from random import randint

# v,n,m = map(int, input().split())
while True:
    print("---")
    v,n,m = randint(1,200),randint(2,10),randint(1,10)
    print(v,n,m)
    ladj = [[] for i in range(n)]
    visitado = [False for i in range(n)]
    custo = [ 200 * 10000 + 1 for i in range(n)]
    tempo = [ 100000000 for i in range(n)]
    chegadadfs = []
    chegadagfs = []
    zero = 0
    for i in range(m):
        a = randint(1,n-1)
        b = randint(a+1,n)
        t = randint(1,500)
        p = 0
        print(a,b,t,p)
        ladj[a-1].append((b-1,t,p))
        ladj[b-1].append((a-1,t,p))
    x = randint(1,n-1)
    y = randint(a+1,n)
    print(x,y)
    depth = deque()
    visitado[x-1] = True
    tempo[x-1] = 0
    dfs(x-1,y-1,0)
    gfs(x-1,y-1,[x-1],0,0)
    if not chegadadfs:chegadadfs = [-1]
    if not chegadagfs:chegadagfs = [-1]
    print(min(chegadadfs),chegadadfs)
    print(min(chegadagfs),chegadagfs)
    print("---")

# for i in range(m):
#     a,b,t,p = map(int, input().split())
#     if not p: zero = 1
#     ladj[a-1].append((b-1,t,p))
#     ladj[b-1].append((a-1,t,p))
# x,y = map(int, input().split())

# depth = deque()
# visitado[x-1] = True
# tempo[x-1] = 0
# # if zero:
# #     dfs(x-1,y-1,0)
# # else:
# gfs(x-1,y-1,[x-1],0,0)
# # print(chegada)
# if not chegada:print(-1)
# else:print(min(chegada))
