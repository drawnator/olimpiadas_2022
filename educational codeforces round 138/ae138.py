def unique(xs,ys):
    if len(xs) == len(set(xs)) and len(ys) == len(set(ys)):
        return True
    return False

def solveRook(i):
    return False

def solveAll(m):
    print(unique(rooksx,rooksy),rooksx,rooksy)
    if unique(rooksx,rooksy):return"YES"
    for i in range(m):
        if solveRook(i):
            return "YES"
    return "NO"

for _ in range(int(input())):
    rooksx = []
    rooksy = []
    a,b = map(int, input().split())
    board = [[-1 for i in range(a+1)] for i in range(a+1)]
    for i in range(b):
        x,y = map(int, input().split())
        board[x][y] = 1
        # rooks.append((x,y))
        rooksx.append(x)
        rooksy.append(y)
    print(solveAll(b))
