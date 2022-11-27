testes = int(input())
contador = 0
atual = "k"
for _ in range(testes):

    controles = list(map(int, input().split()))
    n = controles[0]
    k = controles[1]

    if n - k >= 2:


        print("Kilani")

    else:
        if n == k and n%2 != 1:

            print("Ayoub")
        elif n == k and n%2 == 1:
            print("Kilani")
        elif n - k == 1 and n%2 == 1:
            print("Kilani")
        elif n - k == 1 and n%2 == 0:

            print("Ayoub")
