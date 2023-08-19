p = set()
xs = set()
ys = set()
px = {}
py = {}
ans = set()

def find(p1,p2,p3):
    np1 = (
        p1[0] + (p2[0]-p3[0]),
        p1[1] + (p2[1]-p3[1])
    )
    np2 = (
        p1[0] + (p3[0]-p2[0]),
        p1[1] + (p3[1]-p2[1])
    )
    np3 = (
        p3[0] + (p2[0]-p1[0]),
        p3[1] + (p2[1]-p1[1])
    )
    pr1 = tuple(sorted((p1,p2,p3,np1)))
    if np1 in p and pr1 not in ans:
        ans.add(pr1)
        return 1
    pr2 = tuple(sorted((p1,p2,p3,np2)))
    if np2 in p and pr2 not in ans:
        ans.add(pr2)
        return 1
    pr3 = tuple(sorted((p1,p2,p3,np3)))
    if np3 in p and pr3 not in ans:
        ans.add(pr3)
        return 1
    return 0 

points = []
for i in range(int(input())):
    x,y  = map(int, input().split())
    p.add((x,y))
    points.append((x,y))
    if x not in xs:
        xs.add(x)
        px[x] = [y]
    else:
        px[x].append(y)
    
    if y not in ys:
        ys.add(y)
        py[y] = [x]
    else:
        py[y].append(x)

r = 0
for j in range(len(points)):
    for k in range(j+1,len(points)):
        # 2*pj.x - pk.x
        ## verificar se existe a lista
        ### iterar pela lista e utilizar find
        new_x = 2*points[j][0] - points[k][0]
        if new_x in xs:
            for new_y in px[new_x]:
                new_point = (new_x,new_y)
                if find(points[j],points[k],new_point):
                    r = r + 1
        # 2*pk.x - pj.x
        ## verificar se existe a lista
        new_x = 2*points[k][0] - points[j][0]
        if new_x in xs:
            for new_y in px[new_x]:
                new_point = (new_x,new_y)
                if find(points[j],points[k],new_point):
                    r = r + 1
        # 2*pj.y - pk.y
        ## verificar se existe a lista
        new_y = 2*points[j][1] - points[k][1]
        if new_y in ys:
            for new_x in py[new_y]:
                new_point = (new_x,new_y)
                if find(points[j],points[k],new_point):
                    r = r + 1
        # 2*pk.y - pj.y
        ## verificar se existe a lista
        new_y = 2*points[k][1] - points[j][1]
        if new_y in ys:
            for new_x in py[new_y]:
                new_point = (new_x,new_y)
                if find(points[j],points[k],new_point):
                    r = r + 1


        # for l in range(k+1,len(points)):
        #     # print(points[j],points[k],points[l])
        #     if find(points[j],points[k],points[l]):
        #         r = r + 1

print(r)