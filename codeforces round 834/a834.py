def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def factors(n):
    factors = [[1,1]]
    i = 2
    tn = n
    while tn != 1:
        if not tn%i:
            if factors[-1][0] == i:
                factors[-1][1] = factors[-1][1] + 1
            else:
                factors.append([i,1])
            tn = tn//i
        else:
            i = i + 1
    return factors

def solve(a):
    s = ["Y","e","s"]
    n = -1
    if a[0] == "Y": n = 0
    elif a[0] == "e": n = 1
    elif a[0] == "s": n = 2
    else: return "NO"
    for i in a:
        #print(n,i)
        if not i == s[n]:
            return "NO"
        n = (n+1)%3
    return "YES"

for _ in range(int(input())):
    a = input()
    print(solve(a))
