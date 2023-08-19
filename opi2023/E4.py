p = set()

def find(p1,p2,p3):
    np1 = (
        p1[0] + (p2[0]-p3[0]),
        p1[1] + (p2[1]-p3[1])
    )
    if np1 in p: return 1
    np2 = (
        p1[0] + (p3[0]-p2[0]),
        p1[1] + (p3[1]-p2[1])
    )
    if np2 in p: return 1
    np3 = (
        p3[0] + (p2[0]-p1[0]),
        p3[1] + (p2[1]-p1[1])
    )
    if np3 in p: return 1
    return 0 

points = []
for i in range(int(input())):
    x,y  = map(int, input().split())
    p.add((x,y))
    points.append((x,y))

r = 0
for j in range(len(points)):
    for k in range(j+1,len(points)):
        for l in range(k+1,len(points)):
            # print(points[j],points[k],points[l])
            if find(points[j],points[k],points[l]):
                r = r + 1

print(r//4)