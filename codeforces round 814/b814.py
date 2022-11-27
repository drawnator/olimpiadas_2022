def generate(n,k):
    res = []
    if not k%4:
        return "NO", res
    if (k%4)%2:
        for i in range(1,n,2):
            res.append(f"{i} {i+1}")
    else:
        for i in range(1,n,2):
            if not (i+1)%4:res.append(f"{i} {i+1}")
        for i in range(1,n,2):
            if (i+1)%4:res.append(f"{i+1} {i}")
    return "YES",res

r = []
for i in range(int(input())):
    n,k = map(int, input().split())
    r.append((generate(n,k)))

for ans,list in r:
    print(ans)
    if list != []:print(*list,sep = '\n')
