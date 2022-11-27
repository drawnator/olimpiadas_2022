def bsearch(i,l):
    p1=0
    p2=len(l)
    while p1!=p2:
        m=(p1+p1)//2
        if i<=l[m]:p1=m+1
        else:p2=m
    if i==l[m]:p1-=1
    return p1

def solve(a):
    res = ""
    for i in range(len(a)-2,-1,-1):
        if a[i]!=122 and a[i] == a[i+1]:
            a[i] = a[i]+1
            a.pop()
            bs = bsearch(a[i],a)
            a[i],a[bs] = a[bs],a[i]
        else:
            res = res + chr(a[i+1])
            a.pop()
    res = res + chr(a[0])
    return res[::-1]
a = sorted(list(map(ord,input())),reverse=True)
print(solve(a),sep="")
