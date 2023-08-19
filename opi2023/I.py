cpar = 0
cimpar = 0
rpar = 0
bpar = 0
rimpar = 0
bimpar = 0
l = int(input())
for i,c in enumerate(input()):
    if i%2:
        if c == 'r':
            cpar = cpar + 1
            rimpar = rimpar + 1
        else:
            cimpar = cimpar + 1
            bpar = bpar + 1
    else:
        if c == 'b':
            cpar = cpar + 1
            bimpar = bimpar + 1
        else:
            cimpar = cimpar + 1
            rpar = rpar + 1

# print(cpar,cimpar)
# print(bimpar,rimpar)
# print(bpar,rpar)

# if cpar > cimpar:
#     print(min(bpar,rpar) + abs(bpar-rpar))
# elif cimpar > cpar:
#     print(min(bimpar,rimpar) + abs(bimpar-rimpar))

print(min(min(bpar,rpar) + abs(bpar-rpar),min(bimpar,rimpar) + abs(bimpar-rimpar)))
# else:
#     print(min(abs(bimpar-rimpar),abs(bpar-rpar)))