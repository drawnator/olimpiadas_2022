def check(s,str):
    global a
    if s != 5:return"NO"
    sa = set()
    for i in str:
        sa.add(i)
    if sa == a:
        return "YES"
    return "NO"
a = ["T","i","m","u","r"]
a = set(a)
for i in range(int(input())):
    s = int(input())
    str = input()
    print(check(s,str))
