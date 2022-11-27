def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

for i in range(int(input())):
    a,b,c = map(int, input().split())
    if a == abs(b-c)+c:print(3)
    elif a > abs(b-c)+c: print(2)
    else:print(1)
    # print(min(a,b+c))
