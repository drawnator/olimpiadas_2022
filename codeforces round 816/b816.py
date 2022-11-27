def gen(n,k,b,s):
    # if (n+1)*(k-1)+(k*b) < s:
    #     return [-1]
    # elif k*b > s:
    #     return [-1]

    ar = []
    kb = k*b
    equalizador = kb + min(s-kb,k-1)
    ar.append(equalizador)
    falta = s-equalizador
    while falta > 0 and len(ar) < n:
        # print(ar)
        ar.append(min(k-1,falta))
        falta = falta-ar[-1]
    while len(ar) < n:
        ar.append(0)
    return ar

r = []
ki = []

from random import randint
def soma(ar,s):
    s = 0
    for ai in ar:
        s = s+ai
    return s
def beleza(ar,k):
    s = 0
    for ai in ar:
        s = s + ai//k
    return s

def resposta(n,k,b,s):
    ar = gen(n,k,b,s)
    gb = beleza(ar,k)
    if gb != b:
        return [-1]
    gs = soma(ar,s)
    if gs != s:
        return[-1]
    return ar


# while True:
#     n = randint(1,3)
#     k = randint(1,100)
#     b = randint(1,100)
#     s = randint(1,100)
#     # print(n,k,b,s)
#     generated = resposta(n,k,b,s)
#     gb = beleza(generated,k)
#     if gb == b:
#         print("o",end = "")
#     elif  gb == -1:
#         print(" ",end = "")
#     else:
#         print()
#         print(n,k,b,s,f" - esperado {b} recebeu {gb}")

for _ in range(int(input())):
    n,k,b,s = map(int, input().split())
    r.append(resposta(n,k,b,s))
    # ki.append(k)

for i in r:
    print(*i,sep =" ")
# for i in range(len(r)):
#     print(beleza(r[i],ki[i]))
