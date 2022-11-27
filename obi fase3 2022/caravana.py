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

def solve(n):
    if dp[n] == -1:
        dp[n] = min(solve(n+1)+1,solve(n+2)+1)
    return dp[i]

camelos = []
for _ in range(int(input()) ):
    # dp = [-1 for i in range(int(input()))]
    camelos.append(int(input()))
peso_medio = sum(camelos)//len(camelos)
for unidade in camelos:
    print(peso_medio-unidade)
