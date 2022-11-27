t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    mpar = m%2
    npar = n%2
    if npar != mpar:
        print("Burenka")
    else:
        print("Tonya")
