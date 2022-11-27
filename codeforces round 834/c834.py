def factors(n):
    factors = [[1,1]]
    i = 2
    tn = n
    while tn != 1:
        if not tn%i:
            if factors[-1][0] == i:
                factors[-1][1] = factors[-1][1] + 1
            else:
                factors.append([i,1])
            tn = tn//i
        else:
            i = i + 1
    return factors

def factorial(n):
    div = [[1,-500000]]
    for x in range(1,n+1):
        for xi in factors(x):
            # print(xi)
            if xi[0] > div[-1][0]:
                div.append([xi[0],xi[1]])
            else:
                # print(fbb(div,xi[0]))
                div[fbb(div,xi[0])][1] += xi[1]
    return div

def fbb(a,n):
    p1 = 0
    p2 = len(a)-1
    while p1 != p2:
        mid = (p1+p2)//2
        if a[mid][0] >= n: p2 = mid
        else: p1 = mid+1
    return p1

def bb(a,n):
    p1 = 0
    p2 = len(a)-1
    while p1 != p2:
        mid = (p1+p2)//2
        if a[mid] >= n: p2 = mid
        else: p1 = mid+1
    return p1

from collections import deque

def visinhos(root,x):
    global vis
    alcance = []
    for i in range(len(vis)):
        if abs(root-i) >= x:
            alcance.append(i)
    return alcance

def bfs(root,x):
    global vis
    queue = deque()
    vis[root] = 0
    queue.append(root)
    while queue:
        vertex = queue.popleft()
        for n in range(len(vis)):#visinhos(vertex,x):
            if abs(vertex-n) >= x:
                if vis[n] == -1: #or vis[vertex] + 1 < vis[n]:
                    #print("a ",root,vertex,n)
                    vis[n] = vis[vertex]+1
                    queue.append(n)
def chosepos(l,r,x,a,b):
    if a + x <= b or a-x >= b:
        return b
    if a-x >= l:
        return l
    if a+x <= r:
        return r
    return "b"
def solve(l,r,x,a,b):
    a,b = min(a,b),max(a,b)
    if a==b:return 0
    tries = 0
    while a!=b:
        tries = tries + 1
        a = chosepos(l,r,x,a,b)
        if a == "b":return -1
        # print(l,r,x,a,b)
        # print(a)
        if tries == 4:
            tries = -1
            break
    #print("saida",tries)
    return tries

    # if a == b:return 0
    # elif a-x < l:
    #     print(l,r,x,a,b)
    #     if a+x > r:return -1
    #     if b+x > r:return 3
    #     if a+x <= b: return 1
    #     return 2
    # elif b+x > r:
    #     if b-x < l:return -1
    #     if b+x > r: return 3
    #     if b-x >= a: return 1
    #     return 2
    # elif a+x <= b: return 1
    # elif a-x >= l:return 2
    # elif b+x <= r: return 2

    # global vis
    # sol = 0
    # #if (a==b): return 0
    # bfs(abs(l-a),x)
    # #print(vis)
    # #print("aa",l-a," ",l-b)
    # return vis[abs(l-b)]

res = []
for _ in range(int(input())):
    l,r,x = map(int, input().split())
    #vis = [-1 for i in range(r-l+1)]
    #print(r-l)
    a,b = map(int, input().split())
    res.append(solve(l,r,x,a,b))
print(*res,sep="\n")
