for _ in range(int(input())):
    l = int(input())
    entrada = input()
    s = [i for i in entrada]
    saida = []
    while s:
        c = s.pop()
        # print(c)
        if c == "0":
            second = s.pop()
            first = s.pop()
            char = 10*int(first) + int(second)
            saida.append(chr(96+char))
        else:
            saida.append(chr(96+int(c)))
    print(*saida[::-1],sep = '')
    # print()
