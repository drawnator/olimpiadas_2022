def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(a,b,d):
    x = 1
    fa = a&-a
    fb = b&-b
    fd = d&-d
    if (fa < fd) or (fb < fd):
        return -1
    if a%d == 0 and b%d == 0:
        print(a,b,d,a%d,b%d)
        return 0
    return 0b111111111111111111111111111111 * d


saida = []
t = int(input())
for i in range(t):
    a,b,d = map(int, input().split())
    saida.append(solve(a,b,d))
print(*saida,sep = "\n")
