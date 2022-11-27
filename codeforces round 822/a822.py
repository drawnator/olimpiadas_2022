import math
def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(a,b):
    dif = math.inf
    for i in range(2,a):
        dif = min(b[i]-b[i-2],dif)
    return dif
res = []
for _ in range(int(input())):
    a = int(input())
    b = sorted(list(map(int, input().split())))
    res.append(solve(a,b))
print(*res,sep="\n")
