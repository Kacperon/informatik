import random as r
def tabr(n,l):
    return [[r.randint(1,l)for _ in range(n)]for _ in range(n)]
tab=tabr(10,100)
# tab=[[0,0,10],[10,10,0],[10,10,0]]
def zad20(T):
    n=len(T)
    w,k=[0]*n,[0]*n
    for i in range (n):
        for j in range (n):
            w[i]+=T[i][j]
            k[i]+=T[j][i]
    kordy=(-1,-1,-1,-1)
    sumamax=0
    for i in range (n):
        for j in range (n):
            suma=w[i]+k[j]-2*T[i][j]
            for a in range (i,n):
                for b in range (j,n):
                    sumazap=suma
                    if a!=i and b!=j:
                        suma+=w[a]+k[b]-T[a][b]-T[a][j]-T[i][b]
                    if a==i and b!=j:
                        suma+=k[b]-T[i][b]+T[i][j]
                    if b==j and a!=i:
                        suma+=w[a]-T[a][j]+T[i][j]
                    if suma>sumamax:
                        sumamax=suma
                        kordy=(i,j,a,b)
                    suma=sumazap
                    #end if
    #end for...for
    return(kordy)
print(*tab,sep='\n')
print(zad20(tab))
