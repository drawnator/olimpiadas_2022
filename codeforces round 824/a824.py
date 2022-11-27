import math
def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(a):
    return ((a-3)//3)-1
    
for _ in range(int(input())):
    a = int(input())
    print(solve(a))
