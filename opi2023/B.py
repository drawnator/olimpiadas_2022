n = int(input())
jogos = input()

a = 0
d = 0

for i in range(n):
    if jogos[i] == 'A':
        a += 1
    else:
        d += 1

if a > d:
    print("Angelo")

elif d > a:
    print("DeMatos")
else:
    print("Empate")