def kmex(k):
    global s
    ki = k
    i = 1
    # print(ki in s)
    while ki in s:
        ki = k * i
        i = i + 1
    return ki

s = set()
saida = []
for _ in range(int(input())):
    o,x = input().split()
    if o == "+":
        s.add(int(x))
    else:
        saida.append(kmex(int(x)))
print(*saida,sep="\n")
