def dfs(x,y,n):
    global depth,visitado,chegada
    if x == y:
        chegada.append(n)
    for node in ladj[x]:
        if tempo[node[0]] > n:
            tempo[node[0]] = n
            depth.append((node,n))
    if not depth:return
    new = depth.popleft()
    dfs(new[0][0],y,new[1]+new[0][1])


# def gfs(x,y):
#     global depth,custo,tempo,chegada,ladj
#     depth.append(ladj[x])
#     while depth:
#         i = depth.pop()

def gfs(x,y,caminho,t,p):
    # print(caminho)
    global depth,chegada,v
    if x == y:
        chegada.append(t)
        # print(t)
        # return
    for node in ladj[x]:
        x1 = node[0]
        t1 = node[1]
        p1 = node[2]
        if x1 not in caminho and p + p1 <= v:
            # depth.append((x1,t1,p1))
            gfs(x1,y,caminho+[x1],t + t1,p+p1)
    # if not depth:return
    # new = depth.popleft()
    # gfs(new[0],y,caminho+[new[0]],t + new[1],p+new[2])


import sys
sys.setrecursionlimit(10000000)
from collections import deque

v,n,m = map(int, input().split())
ladj = [[] for i in range(n)]
visitado = [False for i in range(n)]
custo = [ 200 * 10000 + 1 for i in range(n)]
tempo = [ 100000000 for i in range(n)]
chegada = []
zero = 0
for i in range(m):
    a,b,t,p = map(int, input().split())
    if not p: zero = 1
    ladj[a-1].append((b-1,t,p))
    ladj[b-1].append((a-1,t,p))
x,y = map(int, input().split())

# print(ladj)
depth = deque()
visitado[x-1] = True
tempo[x-1] = 0
if zero:
    dfs(x-1,y-1,0)
    if not chegada:print(-1)
    else:print(chegada[0])
else:
    gfs(x-1,y-1,[x-1],0,0)
    if not chegada:print(-1)
    else:print(min(chegada))
# print(chegada)
