import math
def slow(t):
    obj = s(t)//2
    sum = 0
    i = 0
    while sum < obj:
        sum = sum + t-i
        i = i+ 1
    return i

def solve(t):
    obj = s(t)//2
    r = math.floor(t * (1 - 1/(2**(1/2))))
    i = t
    while True:
        print(i)
        if s(t) - s(i) >= obj: return t-i-1
        i = i - 1

def s(n):
    return ((n-1) **2 + (n-1))//2

i = 3
while True:
    i = i +1
    if slow(i) != solve(i):
        print()
        print(i)
    else:print(".",end = "")

t = int(input())
print(solve(t))
