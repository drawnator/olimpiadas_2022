for _ in range(int(input())):
    nome = input()
    nota = sorted(list(map(float, input().split())),reverse=True)[0:3]
    print(f"{nome}: {sum(nota)/max(2,len(nota)):.1f}")
