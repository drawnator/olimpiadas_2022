import math
def d(n):
    numero = 0
    multi = 1
    inicial = 10
    if n < inicial: return (n,0)
    n = n-inicial
    numero = numero + inicial
    inicial = inicial* 9
    multi = multi + 1
    while n > (multi*inicial):
        n = n - (multi*inicial)
        numero = numero + inicial
        multi = multi + 1
        inicial = inicial* 10
    return (int(f"{(n//multi)+numero}"),n%multi)

def make(l,r,k):
    for i in range(r,max(r-10,l),-1)



def solve():

k = int(input())
l,r = map(int, input().split())
print(solve)
