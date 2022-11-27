def check(t,b):
    global trocas
    min1 = t
    max0 = 0
    for i,j in enumerate(b):
        if j^trocas[i]:
            min1 = min(min1,i)
        else:
            max0 = max(max0,i)
    return max0 < min1

def flip(n,t):
    global trocas
    for i in range(n,t):
        trocas[i] = not trocas[i]

def solve(a):
    if a%2:
        return [1 for i in range(a)]
    saida = [0 for i in range(a)]
    for i in range(a//2):
        saida[i] = 1
        saida[-i-1] = 3
    if not (a//2)%2 and a > 2:
        saida[-(a//2)-1] = 2
        saida[(a//2)] = 2
    return saida
    # am3 = a//3
    # saida[am3+1] = 2
    # saida[-am3-1] = 2
    # for i in range(am3):
    #     saida[i] = 1
    #     saida[-i] = 3
    # return saida

def x(a):
    res = 0
    for i in a:
        res = res^i
    return res

def test(n):
    a = solve(n)
    if x(a) == sum(a)/len(a):
        return True
    return False

# for a in range(1,4):
#     for b in range(1,4):
#         for c in range(1,4):
#             for d in range(1,4):
#                 for e in range(1,4):
#                     for f in range(1,4):
#                         for g in range(1,4):
#                             for h in range(1,4):
#                                 for i in range(1,4):
#                                     for j in range(1,4):
#                                         if a^b^c^d^e^f^g^h^i^j == (a+b+c+d+e+f+g+h+i+j)/10:
#                                             print(f"{a} {b} {c} {d} {e} {f} {g} {h} {i} {j}")
# for i in range(1,1000):
#     if not test(i):
#         si = solve(i)
#         print(i)
#         print(*si)
#         print(f"{x(si)}, {sum(si)/len(si)}")
for _ in range(int(input())):
    a = int(input())
    print(*solve(a))
