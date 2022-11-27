import sys
sys.setrecursionlimit(10**7)
def dfs (start):
    global visited,ladj
    if start not in visited:
        visited.add(start)
        for next in ladj[start]:
            dfs(next)
n, m = map(int, input().split())
ladj = [[] for i in range(n)]
for _ in range(m):
    a,b = map(int, input().split())
    ladj[a-1].append(b-1)
sum = 0
for i in range(n):
    visited = set()
    dfs(i)
    sum = sum + len(visited)
print(sum)
