n = int(input())
b = sorted(list(map(int, input().split())))
anteriores = []
p1 = 0
p2 = n-1
vi = abs(b[0]-b[-1])
while p1!=p2:
    print(vi)
    if b[p1+1]-b[p1] > b[p2]-b[p2-1]:
        p1 = p1+1
