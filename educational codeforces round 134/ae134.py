# def mdc(a,b):
#     while a%b != 0:
#         aux = b
#         b = a%b
#         a = aux
#     return b
#
# def mmc(a,b):
#     return (a/mdc(a,b))*b
#
res = []
for _ in range(int(input())):
    st = set()
    a =input()
    c = input()
    st.add(a[0])
    st.add(a[1])
    st.add(c[0])
    st.add(c[1])
    res.append(len(st)-1)
print(*res,sep="\n")
