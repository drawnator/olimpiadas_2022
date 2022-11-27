def solve(a,b):
    m = 0
    for i in b:
        if i == "Q": m = m + 1
        else: m = max(m -1,0)
    if m < 1: return "Yes"
    else: return "No"


for _ in range(int(input())):
    a = int(input())
    b = input()
    print(solve(a,b))
