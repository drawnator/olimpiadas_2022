value = input()
o1 = sum( map(int, list(value)))
o2 = sum( map(int, list(f"{10**len(value)-int(value)}"))) + 1
# print(o1,o2)
print(min(o1,o2))

# value = input()
# o1 = list(map(int, list(value)))
# o2 = list(map(int, list(f"{10**len(value)-int(value)}")))
# print(o1,o2)
# res = 0
# for i in range(len(o1)):
#     res = res + min(o1[i],o2[i]+1)
# # print(o1,o2)
# print(res)
