def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def factors(n):
    if n == 0: return []
    factors = [[1,1]]
    i = 2
    tn = n
    while tn != 1:
        if not tn%i:
            if factors[-1][0] == i:
                factors[-1][1] = factors[-1][1] + 1
            else:
                factors.append([i,1])
            tn = tn//i
        else:
            i = i + 1
    return factors
import math
for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    # print(b)
    n = math.gcd(*b)
    # print(n)
    print(len(factors(n)))
