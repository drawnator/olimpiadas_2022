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
def div(a,b,c,d):
    if a/b == c/d:
        return 0
    if not a or not c:
        return 1
    da = a/b
    dc = c/d
    if (max(da,dc)/min(da,dc)).is_integer():return 1
    return 2

#
# t = int(input())
# for i in range(t):
#     a,b,c,d = map(int, input().split())
#     print(div(a,b,c,d))

# def solve(a,b,c,d):
#     print(a,b,c,d)
#     ab = a/b
#     cd = c/d
#     if ab == cd:
#         return 0
#     if not ab or not cd:
#         return 1
#     print(ab,cd)
#     print(max(ab,cd)/min(ab,cd))
#     if max(ab,cd)/min(ab,cd).is_integer():
#         return 1
#     return 2
for i in range(int(input())):
    a,b,c,d = map(int, input().split())
    ab = a/b
    cd = c/d
    print(div(a,b,c,d))
