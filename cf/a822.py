# import math
# def gcd(a,b):
#     while a%b !=0:
#         aux = b
#         b = a%b
#         a = aux
#     return b
#
# def lcm(a,b):
#     return (a/gcd(a,b))*b

# from math import sum

# def solve(fogo,gelo):
#     if len(fogo) == 0:return sum(gelo)
#     if len(gelo) == 0:return sum(fogo)
#     if gelo[-1] < fogo[-1]:
#         fogo,gelo = gelo,fogo
#     s = 0
#     for i in range(len(gelo)+len(fogo)):
#         print(gelo,fogo,s)
#         if not i%2 and len(gelo) > 0:
#             if len(fogo) > 0:
#                 s = s + 2*gelo.pop()
#             else: s = s + gelo.pop()
#                 # anterior = 0
#         elif len(fogo) > 0:
#             if len(gelo) > 0:
#                 s = s + 2*fogo.pop()
#             else: s = s + fogo.pop()
#             # anterior = 1
#         else:
#             if len(fogo) > 0:
#                 s = s + 2*gelo.pop()
#             else: s = s + gelo.pop()
#     # print(fogo,gelo)
#     return s

# def solve(fogo,gelo):
#     r = 0
#     ultimo = -1
#     while len(fogo) != len(gelo):
#         if len(fogo) > len(gelo):
#             r = r + fogo.pop()
#             ultimo = 0
#         else:
#             r = r + gelo.pop()
#             ultimo = 1
#     if ultimo:iterador = fogo[::-1]+gelo[::-1]
#     else:iterador = gelo[::-1]+fogo[::-1]
#     print(iterador)
#     if ultimo == -1: ultimo = 1
#     else: ultimo = 2
#     for i in range(len(iterador)):
#         print(r)
#         if not i%2:
#             r = r+ultimo*iterador[i//2]
#             ultimo = 2
#             print(r,iterador[i//2])
#         else:
#             r = r+ultimo*iterador[i//2+len(gelo)]
#             ultimo = 2
#             print(r,iterador[i//2+len(gelo)])
#     return r

def solve(fogo,gelo):
    if len(fogo) == 0:return sum(gelo)
    if len(gelo) == 0:return sum(fogo)
    if len(gelo) < len(fogo):fogo,gelo = gelo,fogo
    if len(gelo) == len(fogo) and gelo[-1] < fogo[-1]:
        fogo,gelo = gelo,fogo
    r1 = 0
    last = -1
    while len(fogo)+len(gelo):
        # print(gelo,fogo)
        if len(gelo) > len(fogo):
            s = gelo.pop()
            if last == 0:
                r1 = r1 + 2*s
            else: r1 = r1 + s
            last = 1
        else:
            s = fogo.pop()
            if last == 1:
                r1 = r1 + 2*s
            else:
                r1 = r1 + s
            last = 0
    return r1



for _ in range(int(input())):
    entrada = int(input())
    tipo = list(map(int, input().split()))
    dano = list(map(int, input().split()))
    gelo = []
    fogo = []
    for i,j in enumerate(tipo):
        if j == 0:
            gelo.append(dano[i])
        else:
            fogo.append(dano[i])
    fogo.sort(reverse = True)
    gelo.sort(reverse = True)
    # print(fogo,gelo)
    print(solve(fogo,gelo))
