def solve(l):
    count = 0
    for i in l:
        if alvo[i]:
            alvo[i]  = alvo[i] -1
            alvo[i-1] = alvo[i-1] + 1
        else:
            alvo[i-1] = alvo[i-1] + 1
            count = count + 1
    return count 
n = int(input())
l = list(map(int, input().split()))
alvo = [0 for i in range(1000000+1)]
print(solve(l))