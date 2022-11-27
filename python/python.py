import collections
import sys
import math
sys.setrecursionlimit(10**6)

def gcd(a,b):
    while a%b !=0:
        aux = b
        b = a%b
        a = aux
    return b

def lcm(a,b):
    return (a/gcd(a,b))*b

def find(map):
    biggest = []
    for row in map:
        biggest.append(sizeline(row))
    return biggest

def sizeline(row):
    count = 0
    big = 0
    for item in row:
        if item == 1:
            count += 1
            big = max(big,count)
        else: count = 0
    return big

def divisores(n):
    divisores=[]
    i=1
    while i<=math.sqrt(n):
        if (n % i == 0):
            if(n/i==i):
                divisores.append(i)
            else:
                divisores.append(i)
                divisores.append(int(n/i))
        i=i+1

def menorCrivo(n):
    for i in crivo:
        if not n%i:return i

def crivo(n):
    prime = [True for i in range(n+1)]
    p = 2
    while (p**2<=n):
        if (prime[p] == True):
            for i in range(p**2, n+1, p):
                prime[i] = False
        p += 1
    return prime

def fact(n):
    if n == 1:
        return 1
    return fact(n-1)*n

def fact2(n):
    r = 1
    for i in range(1,n+1):r=r*i
    return r

def fact3(n):
    for i in range(1,n):n=n+i
    return n

def cresc(lista):
    mini = lista[0]
    for i,e in enumerate(lista):
        if mini < e:
            return True
        mini = min(mini,e)
    return False

def connect(n):
    return(int(n*(n-3)/2)+n)

def flip(m):
    n = [[0 for i in range(len(m))] for j in range(len(m))]
    for i in range(len(m)):
        for j in range(len(m[i])):
            n[j][i] = m[i][j]
    return n

def count(m):
    n = flip(m)
    r = 0
    for i in range(len(m)):
        for j in range(len(m[i])):
            if n[i][j] != m[i][j]:r+=1
    return r

def wolf(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            if m[i][j] == "W":
                if i > 0:
                    # m[i-1][j] = "A"
                    if m[i-1][j] == "S":return(False)
                if i < len(m)-1:
                    # m[i+1][j] = "A"
                    if m[i+1][j] == "S":return(False)
                if j > 0:
                    # m[i][j-1] = "A"
                    if m[i][j-1] == "S":return(False)
                if j < len(m[i])-1:
                    # m[i][j+1] = "A"
                    if m[i][j+1] == "S":return(False)
            elif m[i][j] != "S":
                m[i][j] = "D"
    return(True)

def longest(graph,root):
    queue = collections.deque([(root,0)])
    visit_order = []
    levels = []
    visitado[root] = True
    while queue:
        vertex,level = queue.popleft()
        visit_order.append(vertex)
        levels.append(level)
        for node in graph[vertex]:
            if not visitado[node]:
                visitado[node] = True
                queue.append((node,level + 1))
    return levels

def transformation(a,b,l):
    l.append(b)
    while b != a:
        if not b: return False
        elif not b%2:
            b = int(b/2)
        elif f"{b}"[-1] == "1":
            b = int(b/10)
        else:return False
        l.append(b)
    return True

def solve(a,x):
    i = [x-a[-1]+a[0]-1]
    for j in range(len(a)-1):
        i.append(a[j+1]-a[j]-1)
    i.sort(reverse=True)
    r = 0
    for j,k in enumerate(i):
        # print(k,j,4*j)
        adi = k-(4*j)
        if  adi > 1:
            adi -= 1
        adi = max(adi,0)
        r += adi
    # print(a)
    # print(i)
    # print("-")
    return x-r

def res(a):
    res = 0
    for i in a:
        if i > res:
            res = res + 1
    return res

def multi(l,a,b):
    r = 1
    for i in l[a:b]:
        if i > 0: i = 1
        if i < 0: i = -1
        r = r * i
    return r

def db(b):
    esquerda = 0
    loops = 0
    direita = 0
    while b:
        # print(b,esquerda,direita,loops)
        l = b.pop()
        if l == ')':
            esquerda = esquerda + 1
        else:
            if esquerda:
                esquerda = esquerda -1
                loops = loops+ 2
            else:
                direita = direita + 1
    return loops

def jump(i):
    pulos = 0
    li = i
    while i < len(a):
        li = i
        i = i+a[i]
        pulos = pulos + 1
        # print("a ",i,pulos)
    return (li+1,pulos)

n,m = map(int, input().split())
a = list(map(int, input().split()))
for i in range(m):
    q = list(map(int, input().split()))
    if q[0] == 1:
        print(*jump(q[1]-1))
    if q[0] == 0:
        a[q[1]-1] = q[2]
