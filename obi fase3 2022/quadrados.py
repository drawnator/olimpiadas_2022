import math,sys,queue,collections
sys.setrecursionlimit(1000000)

def gcd(a,b):
    while a%b != 0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(i):
    if i == 2:
        print(-1)
    elif i%2:
        for j in range(i):
            linha = []
            for k in range(i):
                linha.append(j*i+k+1)
            print(*linha)

    else:
        ultimo = 0
        matriz = []
        for j in range(i):
            linha = []
            if  j == i-1 :
                scol = 0
                for k in range(i-1):
                    scol = scol + matriz[k][0]
                    ultimo = i*matriz[-1][0] - scol -1
            for k in range(i):
                if k == i-1:
                    # print(i*linha[-1],sum(linha))
                    ultimo = i*linha[-1] - sum(linha)
                else:
                    ultimo = ultimo + 1
                linha.append(ultimo)
            matriz.append(linha)

        for linha in matriz:print(*linha)

solve(int(input()))
