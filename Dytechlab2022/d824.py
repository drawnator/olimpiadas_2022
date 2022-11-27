sabc = set()
for _ in range(int(input())):
    fila = []
    n = int(input())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    d = [y[i]-x[i] for i in range(n)]
    d.sort(reverse=True)
    # print(d)
    p1 = 0
    p2 = n-1
    res = 0
    while p1 < p2:
        if d[p1] + d[p2] >=0:
            # print(d[p1],d[p2])
            res = res+1
            p1 = p1+1
            p2 = p2-1
        else:
            p2 = p2-1
    print(res)
