# def solve(a,b):
#     r1 = a*100//8
#     r2 = b*10
#     # print(r1,r2, r1/r2)
#     for i in range(r2,r1+1):
#         # print(i*100//8,i*10)
#         if i*8//100 == a and i//10 == b:
#             return i
#     return -1

def solve(a,b):
    for i in range(1000000):
        if i*8//100 == a and i//10 == b:
            return i
    return -1
a,b = map(int, input().split())
print(solve(a,b))
