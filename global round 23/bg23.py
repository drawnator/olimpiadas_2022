import math
def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b


dp = []
def solve(n,l):
    operations = 0
    p1 = 0
    p2 = n-1
    while p1 <= p2:
        if l[p1]:
            while l[p2] and p1 != p2:
                p2 = p2 - 1
            if not l[p2]:
                l[p2] = 1
                operations = operations + 1
        p1 = p1 + 1
    return operations


for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    dp = [-1 for i in range(n)]
    print(solve(n,l))
