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

def solve(m,n,l):
    l.sort()
    ini = 1
    for i in l:
        while not i == ini:
            n = n-ini
            ini = ini + 1
            if n < 0:
                return "NO"
        ini = ini + 1
    while n > 0:
        n = n-ini
        ini = ini + 1
    if n < 0:
        return f"NO"#,{n},{m}"
    return f"YES"#,{n},{m}"
res = []
for _ in range(int(input())):
    n,m = map(int, input().split())
    l = list(map(int, input().split()))
    res.append(solve(n,m,l))
print(*res,sep="\n")
