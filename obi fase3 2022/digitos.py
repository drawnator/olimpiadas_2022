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

def solve(l):
    n = 1
    li = mklista(l,n)
    while not cresce(li):
        n = n + 1
        li = mklista(l,n)
    return li[0]

def mklista(l,i):
    saida = []
    j = 0
    # for j in range(0,len(l),i):
    while j < len(l):
        numero = 0
        so9 = 1
        digitos = l[j:j+i]
        # print(digitos)
        j = j + i
        for ki,k in enumerate(digitos):
            if k !=9 :so9 = 0
            numero = numero + 10**(len(digitos)-ki-1) * k
            if ki == len(digitos)-1 and so9:
                i = i + 1
        saida.append(numero)
    return saida

def cresce(l):
    for i in range(1,len(l)):
        if l[i]-l[i-1] != 1:
            return False
    return True

def test(a,b):
    from random import randint
    n = randint(2,b-a)
    sreal = randint(a,b+n)
    d = []
    for i in range(sreal,sreal+n):
        for j in f"{i}":
            d.append(int(j))
    if solve(d) != sreal:
        print(d)
        print(solve(d),sreal)
    print(".",end="")
# while True:
#     test(1000,1010)
n = int(input())
d = list(map(int,input().split()))
print(solve(d))
