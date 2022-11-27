def check(t,b):
    global trocas
    min1 = t
    max0 = 0
    for i,j in enumerate(b):
        if j^trocas[i]:
            min1 = min(min1,i)
        else:
            max0 = max(max0,i)
    return max0 < min1

def flip(n,t):
    global trocas
    for i in range(n,t):
        trocas[i] = not trocas[i]

def solve(t,b):
    global trocas
    tr = 0
    for i,j in enumerate(b):
        if check(t,b):
            return tr
        if j:
            tr = tr + 1
            flip(i,t)
        print(trocas)
        print(b)
        print("-")
    return tr


res = []
for _ in range(int(input())):
    t = int(input())
    b = [int(i) for i in input()]
    trocas = [0 for i in range(t)]
    res.append(solve(t,b))
print(*res,sep="\n")
