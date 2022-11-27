n = int(input())
quadrado = []
linhasE = 0
colunaE = 0
somaE = 100*10
somaL = 0
for i in range(n):
    quadrado.append(list(map(int, input().split())))
    somaE = min(sum(quadrado[i]),somaE)
    somaL = max(sum(quadrado[i]),somaL)

for i in range(n):
    for j in range(n):
        if quadrado[i][j] == 0:
            linhasE = i
            colunaE = j

print(somaL-somaE)
print(linhasE+1)
print(colunaE+1)
