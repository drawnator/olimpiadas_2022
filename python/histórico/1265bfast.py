def permutacao(n):
    # print(max(pos[:n]),min(pos[:n]))
    if maxi[n-1]-mini[n-1] ==  n-1:
        return 1
    return 0
#pegar o max e o min pa posição e verificar se o tamanho é igual o numero
m = int(input())
ans = [[] for i in range(m)]
for i in range(m):
    a = int(input())
    b = list(map(int, input().split()))
    c = sorted(b)
    pos = [0 for j in range(a)]
    maxi = [0 for j in range(a)]
    mini = [10000000 for j in range(a)]
    for n,j in enumerate(b):
        pos[j-1] = n
    for j,d in enumerate(c):
        maxi[j] = max(maxi[j-1],pos[j])
        mini[j] = min(mini[j-1],pos[j])
        ans[i].append(permutacao(d))

for i in ans:
    print(*i,sep = '')
