def bsearch(n,ar):
    p1 = 0
    p2 = n
    while p1!=p2:
        m = (p1+p2)//2
        if ar > m*(m-1)//2:p1=m+1
        else:p2=m
    return p1

n,m = map(int, input().split())
a = max(0,n - (2*m))
# b = max(0,n - (m+1))
b = n - bsearch(n,m)

print(a,b)