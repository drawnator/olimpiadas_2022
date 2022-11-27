n,t = map(int, input().split())
a = list(map(int, input().split()))
acumulada = [a[0]]
for i in range(1,n):
    acumulada.append(acumulada[-1] + a[i])
p1 = 0
p2 = 1
msoma = 0
aS = 0
while p1 != n-1:
    if p2 == n:
        break
    if acumulada[p2]-acumulada[p1] <= t:
        aS = aS+1
        p2 = p2+1
        msoma = max(msoma,aS)
    else:
        p1 = p1+1
        aS = aS-1
print (msoma)
