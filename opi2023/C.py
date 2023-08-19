n = int(input())
testes = set(map(int, input().split()))

answer = 0
for i in range(1, 3001):
    if i not in testes:
        answer = i
        break

print(i)