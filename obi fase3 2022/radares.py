import math,sys,queue,collections
sys.setrecursionlimit(1000000)

#q = queue.PriorityQueue()
#d = collections.deque()
def gcd(a,b):
    while a%b != 0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(n):
    if dp[n] == -1:
        dp[n] = min(solve(n+1)+1,solve(n+2)+1)
    return dp[i]

# for _ in range(int(input()) ):
#     dp = [-1 for i in range(int(input()))]
#     camelos.append(int(input()))

def dfs(i):
    global ladj
    visitados[i] = 1
    for j in ladj[i]:
        if not visitados[j]:
            dfs(j)

def bfs(i,prof):
    global ladj,q,mv
    if not visitados[i]:
        visitados[i] = prof
        if prof >= mv[0]:
            mv = (prof,i)
        for j in ladj[i]:
            if not visitados[j]:
                q.append((j,prof))
        # print(i,prof)

def iterate(i):
    q.append((i,0))
    while q:
        proximo,camada = q.popleft()
        bfs(proximo,camada+1)

def solve():
    for grupo in grupos:
        i,j = findpair(grupo)
        if i != -1:
            return [i,j]
    return [-1]

minhoca = True
n,k = list(map(int,input().split()))
mv = (0,0)
visitados = [0 for i in range(n+1)]
q = collections.deque()
ladj = [[] for i in range(n+1)]
for _ in range(n-1):
    ai, bi = map(int,input().split())
    ladj[ai].append(bi)
    ladj[bi].append(ai)
    if abs(bi-ai) != 1:minhoca = False
iterate(1)
longest = mv
visitados = [0 for i in range(n+1)]
mv = (0,0)
iterate(longest[1])
# print(visitados)
if n == 1:
    print(0)
elif not minhoca:
    print(math.ceil( math.ceil((mv[0]-1)/2)/k))
else:
    r = 0
    while n > 0:
        r = r+1
        n = n - (2*k)
    print(r)
