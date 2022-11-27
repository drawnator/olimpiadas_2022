def solve(a,b):
    res = True
    for i in range(len(a)):
        ac = a[i]
        bc = b[i]
        if ac == 'B':
            ac = 'G'
        # print(bc == "B")
        if bc == 'B':
            bc = 'G'
        # print(bc,ac)
        if ac != bc:
            res = False
    if res:
        return "YES"
    return "NO"

for i in range(int(input())):
    res = True
    n = int(input())
    a = input()
    b = input()
    print(solve(a,b))
