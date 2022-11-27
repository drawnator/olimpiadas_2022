def solve(t,n):
    even = 0
    odd = 0
    for i in n:
        if i%2:odd = odd + 1
        else: even = even + 1
    if t%2:
        if not odd%2:
            return "Bob"
        else:
            return "Alice"
    else:
        if even == odd:
            if even%2:
                return "Alice"
            return "Bob"
        else:
            return "Alice"


for _ in range(int(input())):
    t = int(input())
    n = list(map(int, input().split()))
    print(solve(t,n))
