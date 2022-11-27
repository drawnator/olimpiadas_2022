n = int(input())
a = list(map(int, input().split()))
nuts = 0
for i in a:
    nuts += max(0,i-10)
print(nuts)
