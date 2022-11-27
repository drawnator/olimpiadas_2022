for i in range(int(input())):
    fila = []
    entrada = input()
    s1 = ord(entrada[0])
    s2 = ord(entrada[-1])
    dif = s1 - s2
    for j,i in enumerate(entrada[1:-1:]):
        if ord(i) > max(s1,s2) or ord(i) <  min(s1,s2):continue
        fila.append((ord(i),j+1))
    if dif<=0 :fila.sort()
    else: fila.sort(reverse=True)
    fila.insert(0,(s1,0))
    fila.append((s2,len(entrada)-1))
    # print(fila)
    saida = [i[1]+1 for i in fila]
    print(abs(dif),len(fila))
    print(*saida)
