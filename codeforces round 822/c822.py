def solve(a,t):
    sum = 0
    n = 1
    for i in range(1,a+1):
        while (i*n)-1 < a:
            p = (i*n)-1
            tp = t[p]
            if tp == 1:break
            if tp == 0:
                t[p] = 2
                sum = sum + i
            n = n + 1
        # sum = sum + i*(n-1)
        n = 1
    return sum

res = []
for _ in range(int(input())):
    a = int(input())
    b = input()
    t = [int(b[i]) for i in range(a)]
    # crivo = [1 for i in range(a)
    res.append(solve(a,t))
print(*res,sep="\n")
