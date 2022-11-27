def palindromo(texto):
    lt = len(texto)
    for i in range(lt//2):
        if texto[i] != texto[-i-1]:return False
    return True
n = int(input())
c = input()
p1 = 0
p2 = 1
ma = 0
for i in range(n):
    for j in range(i,n+1):
        if palindromo(c[i:j]):
            ma = max(ma,j-i)

# while True:
#     if p2 == n:break
#     else:
#         tam = tam - 1
#         p1 = p1 + 1
print(ma)
