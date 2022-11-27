n = int(input())
t = list(map(int, input().split()))
t.sort()#reverse=True)
permutacoes = [[0,0] for i in range(2**n)]
# print(t)
for i in range(len(permutacoes)):
    permut = f"{bin(i)[2::]:0>{n}}"
    for j in range(len(permut)):
        # print(t[int(j)],end=" ")
        permutacoes[i][int(permut[j])] += t[int(j)]
    # print()
mini = (10**3)*1000
for i in permutacoes:
    # print(i)
    mini = min(max(i),mini)
print(mini)
