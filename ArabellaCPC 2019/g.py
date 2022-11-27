def solve(a):
    res = []
    if not(a-1)%4:
        for i in range(a-1):
            res.append(i+2)
        return res[::-1]+[0]
    # print(a)
    if not a%4:
        for i in range(a//2):
            res.append(i)
            res.append(i+(a//2))
        return res
    if not (a+1)%4:
        for i in range(a-1):
            res.append(i+2)
        return res[::-1]+[1]
    if not a%2:
        for i in range(a//2):
            res.append(i)
            res.append(i+(a//2))
        return res


for i in range(int(input())):
    a = int(input())
    print(solve(a))
