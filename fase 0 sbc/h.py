from math import floor
def cumsum(n):
    return (n*(n+1))//2

def ncartas(n):
    return 2*cumsum(n) + cumsum(n-1)

def solve(n):
    if n == 1: return 0
    anterior = 0
    base = floor((n/2)**(1/2))
    while True:
        if anterior + 1 == base:
            # print(anterior,base,ncartas(anterior),ncartas(base))
            # print(n >= ncartas(base),ncartas(base),n)
            if n >= ncartas(base):
                return base
            else:return anterior
        if ncartas(base) > n:
            base = (base + anterior)//2
        else:
            anterior = base
            base = base * 2
for i in range(int(input())):
    print(solve(int(input())))
