def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

entradas = [int(input()) for i in range(int(input()))]
for i in entradas:
    menorLcm = 1000000000
    menorTupla = (1,i-1)
    for j in range(1,(i//2)+1):
        Alcm = lcm(j,i-j)
        if Alcm < menorLcm:
            menorLcm = Alcm
            menorTupla = (j,i-j)
    print(menorTupla[0],menorTupla[1])
