res = []
for _ in range(int(input())):
    n,m,sx,sy,d = map(int, input().split())
    r = (n-1) + (m-1)
    if n-sx <=d and sx-1 <= d:
        r = -1
    if m-sy <=d and sy-1 <= d:
        r = -1
    if n-sx <=d and m-sy <=d:
        r = -1
    if sx-1 <= d and sy-1 <= d:
        r = -1
    res.append(r)
print(*res,sep="\n")
