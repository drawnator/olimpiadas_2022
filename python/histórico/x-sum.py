def sumdig(matrix,j,m,n):
    if j <= m:
        r = 0
        for i in range(j):
            #print("a",m-j+i,i)
            r += matrix[m-j+i][i]
        return r
    else:
        r = 0
        for i in range(m+n-j):
            #print("b",i,j-m+i)
            r += matrix[j-m+i][i]
        return r

#matrix[m][n]
t = int(input())
for i in range(t):
    n,m = map(int, input().split())
    matrix = []
    for j in range(n):
        matrix.append(list(map(int, input().split())))
    print(matrix)
    mdig = 0
    nmdig = 0
    mcdig = 0
    nmdig = 0
    for j in range(n+m):
        if mdig < sumdig(matrix,j,m,n):
            nmdig()
    print(mdig)
