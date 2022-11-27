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


def solve(a,b):
    if a%2 and not b%2:
        return [-1]

res = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    res.append(solve(a,b))
for i in res:print(*res)
