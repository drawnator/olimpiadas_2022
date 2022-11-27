def asum(n):
    return (n**2 +n)//2

for _ in range(int(input())):
    a = int(input())
    for i in range(a):
        for j in range(i+1):
            if j == 0 or j == i:
                print(1,end=' ')
            else:print(0,end=' ')
        print()
