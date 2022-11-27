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

for i in range(int(input())):
    n,k = map(int, input().split())
    l = list(map(int, input().split()))
    if 1 in l: print("YES")
    else: print("NO")
