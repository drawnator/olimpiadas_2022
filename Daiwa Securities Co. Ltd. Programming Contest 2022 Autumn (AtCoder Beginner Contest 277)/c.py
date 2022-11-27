from collections import deque


def bfs():
    global ladj
    global visitados
    proximas = deque()
    proximas.append(1)
    maior = 1
    while proximas:
        e = proximas.popleft()
        if e not in visitados:
            visitados.add(e)
            if e > maior:
                maior = e
            if e in ladj:
                for i in ladj[e]:
                    proximas.append(i)
    return maior


n = int(input())
ladj = {} #[[] for i in range(100000001)]
visitados = set() #= [0 for i in range(100000001)]
for i in range(n):
    a,b = map(int, input().split())
    if a not in ladj:
        ladj[a] = []
    if b not in ladj:
        ladj[b] = []
    ladj[a].append(b)
    ladj[b].append(a)
print(bfs())
