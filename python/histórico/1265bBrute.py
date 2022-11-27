def permutation(a,b):
    return sorted(a) == sorted(b)
def checklist(a,b,n):
    c = b[:n:]
    for i in range(len(a)):
        for j in range(len(a)):
            # print(a[i:j+1],c)
            if permutation(a[i:j+1],c):
                return '1'
    return '0'

m = int(input())
ans = ['' for i in range(m)]
for i in range(m):
    a = int(input())
    b = list(map(int, input().split()))
    c = sorted(b)
    for d in c:
        ans[i] = ans[i] + checklist(b,c,d)

for i in ans:
    print(i)
