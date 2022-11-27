d = int(input())
a= int(input())
n = int(input())
if n == 1: diaria = d
elif n < 16:
    diaria = d + (n-1)*a
else:
    diaria = d + 14*a
print((32-n)*diaria)
