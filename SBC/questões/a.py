def solve(l):
    count = 0
    l1 = 0
    for i in l:
        if i == "a":
            l1 = l1 + 1
        else:
            if l1 > 1:
                count = count + l1
            l1 = 0
    if l1 > 1:
        count = count + l1
    return count


n = int(input())
l = input()
print(solve(l))
