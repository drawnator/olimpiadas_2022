def pos(n,k,ki):
    si = []
    for i in range(k-1,0,-1):
        si.append(ki[i] - ki[i-1])
    si.append(ki[0]/(n-k+1))
    for i in range(len(si)-1):
        if si[i] < si[i+1]:
            return "No"
    return "Yes"

for _ in range(int(input())):
    n,k = map(int, input().split())
    ki = list(map(int, input().split()))
    print(pos(n,k,ki))
