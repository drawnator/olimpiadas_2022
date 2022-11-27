n,l = map(int, input().split())
diference = 200+100000
pies = [(i+1)+l-1 for i in range(n)]
for i in pies:
    if abs(i) < abs(diference):
        diference = i
print(sum(pies)-diference)
