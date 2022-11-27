import math
def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(n,k,c):
    saida = []
    letras = [0 for i in range(26)]
    for i in c:
        letra = ord(i)-97
        letras[letra] = letras[letra] + 1
    for i in range(k):
        j = 0
        while letras[j] > 0:
            letras[j] = letras[j] -1
            j = j + 1
        saida.append(chr(97+j))
    return saida

for _ in range(int(input())):
    n,k= map(int, input().split())
    c = input()
    print(*solve(n,k,c),sep = '')
