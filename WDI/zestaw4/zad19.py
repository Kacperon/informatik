import random as r
def tabr(n,l):
    return [[r.randint(1,l)for _ in range(n)]for _ in range(n)]

def il(a,b):
    if a==b:
        return 1
    return 0
    
def zad19(T,ilo):
    count=0
    n=len(T)
    for i in range (n):
        for j in range (n):
            if i+1<n and j-2>=0:
                count+=il(T[i][j]*T[i+1][j-2],ilo)
            if i+1<n and j+2<n:
                count+=il(T[i][j]*T[i+1][j+2],ilo)
            if i+2<n and j-1>=0:
                count+=il(T[i][j]*T[i+2][j-1],ilo)
            if i+2<n and j+1<n:
                count+=il(T[i][j]*T[i+2][j+1],ilo)
            #end if
    #end for...for
    return count

tab=tabr(8,10)
print(*tab,sep='\n')
print(zad19(tab,8))