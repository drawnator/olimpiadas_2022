def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def solve(s):
    for i in range(len(s)):
        for j in range(i+1,len(s)+1):
            if s[i:j] == s[i:j][::-1] and not (j-i)%2:
                return "Or not."
    return "Odd."
s = input()
print(solve(s))
