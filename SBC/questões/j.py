def vencedor(joao, maria):
    if maria == 23:
        return True
    
    elif joao > 23 and maria <= 23:
        return True

    else:
        return False

n = int(input())
cartas_joao = list(map(int, input().split()))
cartas_maria = list(map(int, input().split()))

cartas = {"1": 4, "2": 4, "3": 4, "4": 4, "5": 4, "6": 4, "7": 4, "8": 4, "9": 4, "10":16}

soma_maria = 0
soma_joao = 0

for i in range(2):
    if cartas_maria[i] > 10:
        soma_maria += 10
        cartas["10"] -= 1
    
    else:
        soma_maria += cartas_maria[i]
        cartas[str(cartas_maria[i])] -= 1

    if cartas_joao[i] > 10:
        soma_joao += 10
        cartas["10"] -= 1

    else:
        soma_joao += cartas_joao[i]
        cartas[str(cartas_joao[i])] -= 1

comuns = list(input().split())
for numero in comuns:
    if int(numero) > 10:
        cartas["10"] -= 1
        soma_joao += 10
        soma_maria += 10

    else:
        cartas[numero] -= 1
        soma_joao += int(numero)
        soma_maria += int(numero)

found = False
resposta = 0
for i in range(1, 11):
    if not found:
        if vencedor(soma_joao+i, soma_maria+i) and cartas[str(i)] > 0:
            found = True
            resposta = i

if found:
    print(resposta)

else:
    print(-1) 