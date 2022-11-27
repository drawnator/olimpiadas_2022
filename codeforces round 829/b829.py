import sys,math,random
sys.setrecursionlimit(1000000)

def solve(a):
    saida = []
    if not a%2:
        for i in range((a//2),0,-1):
            saida.append(i)
            saida.append((a//2)+i)
    else:
        saida.append((a//2)+1)
        for i in range(1,(a//2)+1):
            saida.append(i)
            saida.append((a//2)+i+1)
    return saida

def calculate(l):
    m = 1002
    for i in range(len(l)-1):
        m = min(m,abs(l[i]-l[i+1]))
    return m

def brute(a):
    res = [i for i in range(1,a+1)]
    r = 0
    mres = []
    for i in range(100000):
        random.shuffle(res)
        # print(res)
        cr = calculate(res)
        if cr > r:
            r = cr
            mres = res[::]
    return mres

def teste():
    for i in range(2,1001):
        print(i)
        s1 = solve(i)
        s2 = brute(i)
        if calculate(s1) < calculate(s2):
            print(s1,calculate(s1))
            print(s2,calculate(s2))

# teste()
for _ in range(int(input())):
    a = int(input())
    res = solve(a)
    print(*res)
