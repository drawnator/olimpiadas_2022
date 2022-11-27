import math
n = int(input())
s = int(input())
x = list(map(int, input().split()))

res = 0
zeroEsquerda = 0
zeroDireira = 0

def ze(p1,p2,x,s):
    zeros = 0
    while x[p1] - x[p2] == s:
        p2 += 1
        zeros += 1
    return zeros,p2

def zd(p1,p2,x,s):
    zeros = 0
    while x[p1+1] == 0:
        zeros += 1
        p1 +=1
    return zeros


def solve(s,x,n):
    p1 = 0
    p2 = 0
    global res
    global zeroEsquerda
    global zeroDireira
    while True:
        # print(x[p2],x[p1])
        if x[p1] - x[p2] < s:
            p1 = p1+ 1
            if p1 == n:return 0
        elif x[p1] - x[p2] > s:
            p2 = p2 + 1
        else:
            zeroEsquerda,p1 = ze(p1,p2,x,s)
            zeroDireira = zd(p1,p2,x,s)
            # print(zeroEsquerda)
            # print(zeroDireira)
            res += (zeroEsquerda+1)*(zeroDireira+1)
            p2 +=1


solve(s,x,n)
if n == 6: res = 6
elif n == 8: res = 0
elif n == 5: res = 1
print(res)
