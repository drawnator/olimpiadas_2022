def lenta(a,b,c,d):
    for _ in range(d[-1]):
        for j in range(b):
            for i in range(a):
                if j != b-1: c[i] = c[i] + d[j+1]
                c[i] = c[i]%d[j]
            # print(*c)
    zerado = 1
    r1 = c[0]
    for i in c:
        if r1 != i:
            zerado = 0
            break
    if zerado: return "YES"
    else: return "NO"


def rapida(a,b,c,d):
    # if d[-1] > 3:
    dif = d[-1] - 3
    for i in range(b):d[i]=d[i]-dif
    # print(d)
    for _ in range(d[-1]):
        for j in range(b):
            for i in range(a):
                if j != b-1: c[i] = c[i] + d[j+1]
                c[i] = c[i]%d[j]
            # print(*c)
    zerado = 1
    r1 = c[0]
    for i in c:
        if r1 != i:
            zerado = 0
            break
    if zerado: return "YES"
    else: return "NO"

def gerar():
 a,b = randint(1,10),randint(1,10)
 c = [randint(1,100) for i in range(a)]
 d = sorted([randint(1,100) for i in range(b)],reverse=True)
 # print(a,b)
 # print(c)
 # print(d)
 if rapida(a,b,c,d) != lenta(a,b,c,d):
     print()
     print(a,b,c,d)
     return True
 else:
     print(".",end="")
     return False

from random import randint
while True:
    if gerar():break
    # input()

# def gcd(a,b):
#     while a%b !=0:
#         aux = b
#         b = a%b
#         a = aux
#     return b
#
# def lcm(a,b):
#     return (a/gcd(a,b))*b

a,b = map(int, input().split())
c = list(map(int, input().split()))
d = sorted(list(map(int, input().split())),reverse=True)
if d[-1] > 4 : print(rapida(a,b,c,d))
else: print(lenta(a,b,c,d))
