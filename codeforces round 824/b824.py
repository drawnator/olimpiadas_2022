import sys,math
sys.setrecursionlimit(1000000)

res = []
for _ in range(int(input())):
    a = int(input())
    b = list(map(int, input().split()))
    smallest = min(b)
    res.append(sum([max(0, math.ceil((i-((2*smallest)-1))/((2*smallest)-1))) for i in b]))
print(*res,sep="\n")
