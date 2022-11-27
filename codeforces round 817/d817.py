sabc = set()
for _ in range(int(input())):
    fila = []
    k = int(input())
    a = list(input())
    for i in range(len(a)):
        if a[i] == "R":
            fila.append(len(a)-i-1)
        else:
            fila.append(i)
    setfila = sorted(fila)[0:k]
    # print(fila,sum(fila))
    res = []
    for i in range(len(fila)):
        if fila[i] in setfila:
            setfila.remove(fila[i])
            bsum = sum(fila)
            fila[i] = max(fila[i],len(a)-fila[i]-1)
            if len(res):
                res.append(sum(fila)-bsum)
            else:
                res.append(0)
                saida = [sum(fila)]
    for i in sorted(res,reverse=True):
        saida.append(saida[-1]+i)

    print(*saida[:-1:],sep= ' ')
