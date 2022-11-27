
l = list(map(int, input().split()))
n = l[0]
c = l[1]
final = []
palavras = []
termos = []
resp =0
for a in range(n):
    palavras.append(list(input()))
for b in range(n):
    
    for t in range(c):
        if palavras[b][t] == "*":
            for r in range(26):
                palavras[b][t] = chr(97 + r) 
                # print(palavras[b])
                
                x = ''.join(palavras[b])
                termos.append(x)

def contar(termos):
    dict = {}
    maxi = 1
    big = []
    for i in termos:
        if i in dict:
            dict[i] = dict[i] + 1
            maxi = max(dict[i],maxi)
        else:
            dict[i] = 1
    for i in dict:
        if dict[i] == maxi:
            big.append(i)
    return sorted(big)[0],maxi


# contar(sorted(termos))
print(*contar(sorted(termos)))
# for p in range(n):
#     for q in range(c):
#         if palavras[p][q] != final[q] and palavras[p][q] != "*":
#             break
#         elif q + 1 == c:
#             resp += 1


# print(*final,sep="",end = " ")
# print(resp)


