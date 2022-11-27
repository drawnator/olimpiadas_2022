n = int(input())
l = []
d1 = True
d2 = True
d3 = True
for i in range(n):
    s = input()
    if s[0] not in ["H","D","C","S"]:
        d1 = False
        break
    if s[1] not in ["A","2","3","4","5","6","7","8","9","T","J","Q","K"]:
        d2 = False
        break
    if s in l:
        d3 = False
        break
    l.append(s)

if (d1 and d2 and d3):
    print("Yes")
else:
    print("No")


