sabc = set()
for _ in range(int(input())):
    m = {}
    n = int(input())
    a = list(input().split())
    b = list(input().split())
    c = list(input().split())
    for i in a+b+c:
        if i in m:
            m[i] = m[i]+1
        else:
            m[i] = 1
    pa = 0
    pb = 0
    pc = 0
    for i in a:
        if m[i] == 1:
            pa = pa + 3
        if m[i] == 2:
            pa = pa + 1
    for i in b:
        if m[i] == 1:
            pb = pb + 3
        if m[i] == 2:
            pb = pb + 1
    for i in c:
        if m[i] == 1:
            pc = pc + 3
        if m[i] == 2:
            pc = pc + 1
    print(pa,pb,pc)
