n = int(input())
p = [[min(j+1,n-j,i+1,n-i) for j in range(n)] for i in range(n)]
for i in p:print(*i)
