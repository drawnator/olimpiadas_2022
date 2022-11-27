from random import randint
#
# def gprimes(n):
#     primes = [2]
#     for i in range(3,n+1,2):
#         if vprime(i,primes):
#             primes.append(i)
#     primes.append(1)
#     return primes
#

# def solve(a,b):
#     for i in range(a,b-1):
#         for j in range(i+1,b):
#             # print(f'- {i},{j}')
#             if a <= lcm(i,j) and b >= lcm(i,j):
#                 return(i,j)
#     return(-1,-1)
#
# def bSolve(a,b):
#     for i in range(a,b//2):
#         for j in range(i+1,b):
#             # print(f'- {i},{j}')
#             if a <= lcm(i,j) and b >= lcm(i,j):
#                 return(i,j)
#     return(-1,-1)
#
#
# def gcd(a,b):
#     while a%b !=0:
#         aux = b
#         b = a%b
#         a = aux
#     return b
#
# def lcm(a,b):
#     return (a/gcd(a,b))*b
#
def vprime(n,primes):
    for i in primes:
        if n%i == 0: return False
    return True

def find(n,div):
    for i in range(len(div)):
        if div[i] == n:return i

def sSolve(r):
    s = 0
    while r != 0:
        s += 1
        r -= menorDivisor(r)
    return s

def fSolve(r):
    s = 0
    if r != 0:
        s += 1
        r -= menorDivisor(r)
    s += int(r//2)
    return s

def menorDivisor(n):
    for i in range(2,int(n**(1/2))+1):
        if not n%i:return i
    return n

# def divisores(n):
#     div  = set()
#     for i in range(1,int(n**(1/2))+1):
#         if not n%i:
#             div.add(i)
#             div.add(int(n/i))
#             if len(div) > 3:break
#     return div

loops = int(input())
test = list(map(int, input().split()))
for i in test:
    if len(divisores(i)) == 3:print("YES")
    else:print("NO")

# while True:
#     r = randint(2,int(10e10))
#     print(r)
#     s1 = sSolve(r)
#     s2 = fSolve(r)
#     print(s2)#,s2)
#     # print(s1 == s2)


# while True:
#     a = randint(1,10000)
#     b = randint(a,10001)
#     print(a,b)
#     ans1 = solve(a,b)
#     ans2 = bSolve(a,b)
#     if not (ans1 == ans2 ):
#         print(ans1,ans2)
#         print()
#
# e = [int(input()) for i in range(int(input()))]
# for i in e:print(int((i/s(i))),i-int((i/s(i))))
