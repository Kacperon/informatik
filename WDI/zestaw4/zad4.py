import random as r
from time import time
start=time()
def tabr(n,l):
    return [[r.randint(1,l)for _ in range(n)]for _ in range(n)]
    
def zad4(t):
    l=len(t)
    tw,tk=[0]*l,[0]*l
    for i in range (l):
        for j in range(l):
            tw[i]+=t[i][j]
            tk[i]+=t[j][i]
    sumaw,sumak=0,tk[0]
    w,k=0,0
    for i in range(l):
        if tw[i]>sumaw:
            sumaw=tw[i]
            w=i
        if tk[i]<sumak:
            sumak=tk[i]
            k=i
    return(w,k,sumaw,sumak,sumaw/sumak)
t2=tabr(2000,100)
# print(*t2,sep='\n')
print(zad4(t2))
print(time()-start)