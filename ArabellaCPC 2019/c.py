testes = int(input())


final = []
palavras = list(input())
teclas = int(input())
tamanho = "m"

for a in range(teclas):
    atual = input()
    if atual == "Backspace" and len(final) > 0:
        final.pop()
    elif atual == "Backspace" and len(final) <= 0:
        tamanho = tamanho
    elif atual == "CapsLock" and tamanho == "m":
        tamanho = "g"
    elif atual == "CapsLock" and tamanho == "g":
        tamanho = "m"
    elif atual == "Space":
        final.append(" ")
    else:
        if tamanho == "g":
            final.append(atual.upper())
        else:
            final.append(atual)
if list(palavras) == final:
    print("Correct")
else:
    print("Incorrect")
