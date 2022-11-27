import sys,math
sys.setrecursionlimit(1000000)

def solve(a,b):
    res = 0
    p1 = math.floor(b**(1/2))
    p2 = math.ceil(a**(1/2))
    sq = p1 - p2
    res = res + 2*sq + sq+1
    p3 = math.floor(a**(1/2))
    # print(math.floor((a-math.floor(a**(1/2))**2)/math.floor(a**(1/2))))
    # 2 - math.floor((a-math.floor(a**(1/2))**2)/math.floor(a**(1/2)))
    res = res + math.floor((b-p1**2)/p1)
    res = res + 2 - math.floor((a-p3**2-1)/p3)
    return res
res = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    res.append(solve(a,b))
print(*res,sep = "\n")
