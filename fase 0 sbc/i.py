def equation(n,k,p,x):
    return x*n + p*k/n

import math
k,p,x = map(int, input().split())
ea = eb = ec = equation(math.inf,k,p,x)
n = 0
while ea <= eb or ec <= eb:
    n = n + 1
    ea = eb
    eb = ec
    ec = equation(n,k,p,x)

print(f"{eb:.3f}")
