def dis2words(w1,w2):
    s = 0
    for i in range(len(w1)):
        s += abs(ord(w1[i])-ord(w2[i]))
    return s


a = int(input())
res = []
for i in range(a):
    b,c = map(int, input().split())
    last = []
    mini = int(10e20)
    for i in range(b):
        word = input()
        for word2 in last:
            dis = dis2words(word,word2)
            if dis < mini:
                mini = dis
        last.append(word)
    res.append(mini)



    #     size = 0
    #     for i in input():
    #         size += ord(i)
    #     sizes.append(size)
    # sizes.sort()
    # for i in range(1,b):
    #     if abs(sizes[i] - sizes[i-1]) < mini:
    #         mini = abs(sizes[i] - sizes[i-1])
    # res.append(mini)
print(*res,sep='\n')
