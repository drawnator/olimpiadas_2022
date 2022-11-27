def correto(palavre,dic,pr):
    re = False
    for i in range(5):
        if dic[i] == palavra:
            re = True
            pr[i] = 1.0
    return re

def dif(i,palavra):
    dis = max(0,len(i)-len(palavra))
    for j in palavra:
        f = i.find(j)
        print(i,j,f)
        if f != -1:
            i = i[0:f]+i[f+1::]
        else :dis=dis+1
    # dis = dis + len(i)
    return dis

pt = [0 for i in range(5)]
for _ in range(int(input())):
    palavra = input()
    dic = input().split()
    pr = [0 for i in range(5)]
    dis = []
    if not correto(palavra,dic,pr):
        for i in dic:
            dis.append(dif(i,palavra))
        print(dis)
        threshold = min(dis)
        for i in range(5):
            if dis[i] == threshold:
                pr[i] = 0.5
    pt = [pt[i]+pr[i] for i in range(5)]
    print(pt)
pr = max(pt)
print(pr)
print(*pt)
