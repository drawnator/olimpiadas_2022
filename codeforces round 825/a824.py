def solve(l1,l2):
    re = 0
    operations = 0
    pl1 = 0
    for i in range(len(l1)):
        if l1[i] and not l2[i]:
            if pl1 < 0:
                re = 1
            pl1 = pl1 + 1
        if not l1[i] and l2[i]:
            pl1 = pl1 - 1
            if pl1 > 0:
                re = 1
    return abs(pl1) + re


for _ in range(int(input())):
    n = int(input())
    l1 = list(map(int, input().split()))
    l2 = list(map(int, input().split()))
    print(solve(l1,l2))
