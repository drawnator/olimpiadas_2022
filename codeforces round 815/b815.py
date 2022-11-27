def solve():
    return 0

for i in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    mai = 0
    mai2 = 0
    men = 10000000000
    men2 = 10000000000
    for i in range(n):
        if l[i] >= mai:
            mai2 = mai
            mai = l[i]
        elif l[i] >= mai2:
            mai2 = l[i]
        if l[i] <= men:
            men2 = men
            men = l[i]
        elif l[i]  <= men2:
            men2 = l[i]
    # print(mai,mai2,men,men2)
    print(mai+mai2-men-men2)
