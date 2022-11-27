n,m = map(int, input().split())

def mod(n):
    return int(n)%m

l = list(map(mod, input().split()))
l.sort()
mcresc = 0
d = 0
e = 0
for i in range(n-1):
    if l[i] <= l[i+1]:
        e = e + 1
    else:break
for i in range(n-1,0,-1):
    if l[i] >= l[i-1]:
        e = e + 1
    else: break
for i in range(n-1):
    mt = 0
    if l[i] <= l[i+1]:
        mt = mt + 1
    else:
        mcresc = max(mcresc,mt)
        mt = 0
mcresc = max(mcresc,mt)
mcresc = max(e+d,mcresc)
print(mcresc)

