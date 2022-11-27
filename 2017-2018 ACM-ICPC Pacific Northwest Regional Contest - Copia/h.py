n, k = map(int, input().split())

if n == 1 or n < k:
    print(10)

else:
    if n%k > 0:
        print((n//k + 1) * 5)
    else:
        print((n//k) * 5)
