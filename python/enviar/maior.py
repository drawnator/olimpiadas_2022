def solve(n,m,s):
    for i in range(m,n-1,-1):
        sum = 0
        for j in f'{i}':
            sum += int(j)
        if sum == s: return i
    return -1

n = int(input())
m = int(input())
s = int(input())
print(solve(n,m,s))
