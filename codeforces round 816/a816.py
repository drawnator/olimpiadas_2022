# def mdc(a,b):
#     while a%b != 0:
#         aux = b
#         b = a%b
#         a = aux
#     return b
#
# def mmc(a,b):
#     return (a/mdc(a,b))*b
#
res = []
for _ in range(int(input())):
    a,b = map(int, input().split())
    a,b = max(a,b),min(a,b)
    r = 2*(b-1)+a
    if a == 1:
        r = 0
    res.append(r)

print(*res,sep="\n")
