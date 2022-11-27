# 08 may 2022
# guilherme Silva Toledo
# compare 2 programs outputs

import os
from random import randint
from sys import stdin, stdout

def randomizarLista(L):
    for i in range(len(L)):
        r = randint(i,len(L)-1)
        L[i],L[r] = L[r], L[i]

#create "tn" file with random test cases
def winput(testfile):
    # input creator
     with open(f"{testfile}","w") as f:
         n,m = randint(1,100000),randint(1,100000)
         f.write(f"{n} {m}")
         f.write("\n")
         # r = [randint(-10,10) for j in range(1,n+1)]
         # randomizarLista(r)
         r = [randint(1,n) for i in range(n)]
         sb = ' '.join(map(str,r))
         f.write(f'{sb}\n')
         # m = randint(1,10000)
         # f.write(f"{m}\n")
         for i in range(m):
             q = randint(0,1)
             if q:
                 f.write(f"1 {randint(1,n)}\n")
             else:
                f.write(f"0 {randint(1,n)} {randint(1,n)}\n")
             # l = randint(1,n)
             # r = randint(l,n)
             # f.write(f'{l} {r}\n')
         # r = [randint(-10,10) for j in range(1,n+1)]
         # randomizarLista(r)
         # sb = ' '.join(map(str,r))
         # f.write(f'{sb}\n')
         # for i in range(k):
         #     o = randint(0,1)
         #     if o: f.write(f'C {randint(1,n)} {randint(-10,10)}\n')
         #     else:
         #         p1 = randint(1,n-1)
         #         p2 = randint(p1,n)
         #         f.write(f'P {p1} {p2}\n')
    # a = randint(1,10)
    # with open(f"{testfile}","w") as f:
    #     f.write(f"{a}\n")
    # for i in range(a):
    #     b = randint(1,100)
    #     lb = [j for j in range(1,b+1)]
    #     randomizarLista(lb)
    #     sb = ' '.join(map(str,lb))
    #     with open(f"{testfile}","a") as f:
    #         f.write(f"{b}\n")
    #         f.write(f"{sb}\n")

# save normal and bruteforce solutions to "outfast" and "outbrute" files
def winout(language1,language2, program1, program2,testfile,output1,output2):
    os.system(f"{language1}{program1} < {testfile} > {output1}")
    os.system(f"{language2}{program2} < {testfile} > {output2}")

# test if both outputs are equal
def wintest(output1,output2):
    with open(output1,"r") as outfast:
        with open(output2,"r") as outbrute:
            a = outfast.read()
            b = outbrute.read()
            if a != b:
                return False
            return True

#create a copy of the tn file on the error folder
def copy(loop,testfile):
    with open(testfile,"r") as fin:
        with open(f"error/tn{loop}","w") as fout:
            fout.write(fin.read())

#main loop
def main(language1,language2,testcases,testfile,program1,program2,output1,output2):
    for loop in range(testcases):
        winput(testfile)
        winout(language1,language2,program1,program2,testfile,output1,output2)
        if not wintest(output1,output2):
            copy(loop,testfile)
            print('\nproblem')
        else:
            if loop%100: print('.', end='', flush=True)
            else: print()

if __name__ == '__main__':
    language1 = "py " #require space after the program(if c leave "" no spaces)
    language2 = ""
    testcases = 1000
    testfile = "tn"
    program1 = "python.py"
    program2 = "hole.exe"
    output1 = "outfast"
    output2 = "outbrute"

    os.system("mkdir error")
    main(language1,language2,testcases,testfile,program1,program2,output1,output2)
