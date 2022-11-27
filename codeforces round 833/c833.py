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

def factorial(n):
    div = [[1,-500000]]
    for x in range(1,n+1):
        for xi in factors(x):
            # print(xi)
            if xi[0] > div[-1][0]:
                div.append([xi[0],xi[1]])
            else:
                # print(fbb(div,xi[0]))
                div[fbb(div,xi[0])][1] += xi[1]
    return div

def fbb(a,n):
    p1 = 0
    p2 = len(a)-1
    while p1 != p2:
        mid = (p1+p2)//2
        if a[mid][0] >= n: p2 = mid
        else: p1 = mid+1
    return p1

def bb(a,n):
    p1 = 0
    p2 = len(a)-1
    while p1 != p2:
        mid = (p1+p2)//2
        if a[mid] >= n: p2 = mid
        else: p1 = mid+1
    return p1

def solve(a,x):
    print(factorial(x))
    for i in factorial(x):
        if a.count(i[0]) < i[1]:
            return "No"
    return "Yes"

n,x = map(int, input().split())
a = list(map(int, input().split()))
print(solve(a,x))
