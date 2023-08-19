n = int(input())
nums = []
m = {}
out = 0
for i in range(n):
    a,b = map(int, input().split())
    nums.append((a,b))

for i in range(n):
    for j in range(i + 1, n):
        x = nums[i][0] - nums[j][0]
        y = nums[i][1] - nums[j][1]

        if (x,y) in m:
            m[(x,y)] += 1
        else:
            m[(x,y)] = 1


for x in m.values():
    out += x // 2

print(out // 2)