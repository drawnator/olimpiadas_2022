def solve(t,n):
    pos = []
    for i in range(t):
        pos.append([n[i],i])
    pos.sort(reverse=True)
    num = []
    for i in pos:
        num.append(i[1]+1)
    return num

for _ in range(int(input())):
    t = int(input())
    n = list(map(int, input().split()))
    print(*solve(t,n))
