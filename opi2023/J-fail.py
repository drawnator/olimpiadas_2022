a = input()
b = input()
s = set()
if (a==b):
    print("YES")
elif (len(a)==len(b) and len(a)%2==0):
    s.add(a[0:len(a)//2])
    s.add(a[len(a)//2:])
    if b[0:len(a)//2] in s: print("YES")
    elif b[len(b)//2:] in s: print("YES")
    else: print("NO")
else: print("NO")