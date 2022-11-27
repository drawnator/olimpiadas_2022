def bb(l,k):
    # print(l,k)
    p1 = 0
    p2 = len(l)
    while p1!=p2:
        m = (p1+p2)//2
        if k>=l[m]:p1=m+1
        else:p2=m
    return p1

for i in range(int(input())):
    n,q = map(int, input().split())
    a = list(map(int, input().split()))
    w = []
    wc = [[] for i in range(n+1)]
    c = a[0]
    for i in range(1,len(a)):
        c = max(c,a[i])
        wc[c].append(i)
        w.append(c)
    # print(wc)
    for i in range(q):
        i,k = map(int, input().split())
        # print("a", i,k,a[i-1],n)
        # print(a[i-1])
        busca = bb(wc[a[i-1]],k)
        if a[i-1] == n:
            busca = busca + max(0,k-n+1)
        print(busca)
