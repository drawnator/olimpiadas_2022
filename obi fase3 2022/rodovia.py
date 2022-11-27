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
    grupos[-1].append(i)
    for j in ladj[i]:
        if not visitados[j]:
            dfs(j)

def bfs():return 0

def findpair(grupo):
    for i in range(len(grupo)-1):
        for j in range(i+1,len(grupo)):
            # print(grupo[i],grupo[j])
            if grupo[j] not in ladj[grupo[i]]:
                return grupo[i],grupo[j]
    return -1,-1

def solve():
    for grupo in grupos:
        i,j = findpair(grupo)
        if i != -1:
            return [i,j]
    return [-1]

n,k = list(map(int,input().split()))
grupos = []
visitados = [0 for i in range(n+1)]
ladj = [[] for i in range(n+1)]
for _ in range(k):
    ai, bi = map(int,input().split())
    ladj[ai].append(bi)
    ladj[bi].append(ai)

for i in range(n):
    if not visitados[i]:
        grupos.append([])
        dfs(i)

print(*solve())
