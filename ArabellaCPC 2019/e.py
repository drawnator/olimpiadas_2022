# p1 = 3
# p2 = 10 ** 18-1 #1000000000000000000
# lp2 = p2
# while p1 != p2:
#     print(f"? {p1} {p2}")
#     m = (p1 + p2)//2
#     if int(input()) == -1:
#         lp2 = p2
#         p2=m
#     else:
#         p1=p2
#         p2 = lp2
# print(f"! {p1}")
from sys import stdout
ran = 1
rat = 3
perguntas = 1
multi = 2**10
div = 2**6
ulti = rat
while rat != ran and perguntas != 51:
    print(f"? {ran} {rat} ")
    stdout.flush()
    perguntas = perguntas +1
    if int(input()) != -1:
        if multi == 2:
            ran = rat
            rat = ulti
            break
        ran = rat
        rat = rat*multi
        ulti = rat
    else:
        rat = (rat + ran)//div
        div = 2
        multi = 2
# print(f"C {ran} {rat}")
lp2 = rat
while ran != rat:
    print(f"? {ran} {rat}")
    m = (ran + rat)//2
    if int(input()) == -1:
        lp2 = rat
        rat=m
    else:
        ran=rat
        rat = lp2
print(f"! {ran}")
# print(f"? 1 3")
# a = int(input())
# print(f"? 3 1")
# b = int(input())
# print("! {a+b}")
