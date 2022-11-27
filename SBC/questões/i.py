def solve(l):
    for i in l:
        if i == 9:
            return "F"
    return  "S"
l = list(map(int, input().split()))
print(solve(l))
    