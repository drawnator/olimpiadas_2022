import sys
sys.setrecursionlimit(10*6)
def l(s):return s[0:len(s)//2]
def r(s):return s[len(s)//2:]

dp = {}
def solve(a,b):
    m = (a,b)
    if m in dp:
        return dp[m]
    if a == b:
        dp[(a,b)] = True
        dp[(b,a)] = True
        return True
    if len(a) == 1 or len(a)%2 == 1:
        dp[(a,b)] = False
        dp[(b,a)] = False
        return False

    la = l(a)
    ra = r(a)
    lb = l(b)
    rb = r(b)
    if solve(la,lb):
        res = solve(ra,rb)
        dp[(a,b)] = res
        dp[(b,a)] = res
        return res
    elif solve(la,rb):
        res = solve(ra,lb)
        dp[(a,b)] = res
        dp[(b,a)] = res
        return res

m = input()
n = input()
if solve(m,n):
    print("YES")
else:print("NO")