n = int(input())

points = []
for i in range(n):
    coordinates = list(map(int, input().split()))
    points.append(coordinates)

coeficientes = {}
for i in range(n):
    for j in range(n):
        if i != j:
            deltaX = points[i][0] - points[j][0]
            deltaY = points[i][1] - points[j][1]
            coeficiente = deltaX/deltaY

            if coeficiente in coeficientes:
                coeficientes[coeficiente].append([deltaX, deltaY, points[i]])
            else:
                coeficiente[coeficiente] = [[deltaX, deltaY, points[i]]]
print(coeficientes)
# for key in coeficientes.keys:
#     for i in len(key):
#         for j in len(key):
#             if i != j:
#                 deltaX1 = key[i][2][0] - key[i][2][0] 
#                 deltaY1 = key[i][2][1] - key[i][2][1]
#                 coeficiente1 = deltaX1/deltaY1

#                 deltaX2 = key[j][0] - key[j][0] 
#                 deltay2 = 
#                 coeficiente2 = deltaX2/deltaY2
#                 if  


