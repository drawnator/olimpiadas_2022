def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def divisores(n):
    divisores = []
    i = 2
    while i <= n**(1/2):
        if (n%i == 0):
            if (n/i == i):
                divisores.append(i)
            else:
                divisores.append(i)
                divisores.append(int(n/i))
        i= i + 1
    return divisores

def solve(n,m):
    d = divisores(n)
    dois = d.count(2)
    cinco = d.count(5)
    mul = 0
    r = 1
    while dois < cinco or :
    if dois < cinco:
        while r <= m:
            r = r*5
            #mul = mul + 1
        r = int(r/5)
    if:
        while r <= m:
            r = r*2
            #mul = mul + 1
        r = int(r/2)
    if dois == cinco:
        while r <= m:
            r = r*10
            #mul = mul + 1
            r = int(r/10)
    if r == 0:r = m
    return n*r
    # x = 1
    # fa = a&-a
    # fb = b&-b
    # fd = d&-d
    # if (fa < fd) or (fb < fd):
    #     return -1
    # if a%d == 0 and b%d == 0:
    #     print(a,b,d,a%d,b%d)
    #     return 0
    # return 0b111111111111111111111111111111 * d


saida = []
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    saida.append(solve(n,m))
print(*saida,sep = "\n")
