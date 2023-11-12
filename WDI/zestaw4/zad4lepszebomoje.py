import random as r
from time import time
start=time()
def tabr(n,l):
    return [[r.randint(1,l)for _ in range(n)]for _ in range(n)]
    
def zad4(t):
    l=len(t)
    sumaw,sumak=0,float('inf')
    w,k=-1,-1
    for i in range (l):
        swc=0
        skc=0
        for j in range(l):
            swc+=t[i][j]
            skc+=t[j][i]
        if swc>sumaw:
            sumaw=swc
            w=i
        if skc<sumak:
            sumak=skc
            k=i
    
    return(w,k,sumaw,sumak,sumaw/sumak)
t2=tabr(2000,100)
# print(*t2,sep='\n')
print(zad4(t2))
print(time()-start)