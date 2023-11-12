t=[[0]*11 for _ in range(11)]

def spirala(tab):
    l=len(tab)-1
    a,lzap=1,len(tab)
    for i in range (0,int(l//2)+1):
        for j in range(i,l):
            tab[i][j]=a
            a+=1
        for j in range(i,l):
            tab[j][l]=a
            a+=1
        for j in range(l,i,-1):
            tab[l][j]=a
            a+=1
        for j in range(l,i,-1):
            tab[j][i]=a
            a+=1
        l-=1
    if (lzap)%2==1:
        tab[(lzap//2)][(lzap//2)]=(lzap)**2
    return(tab) 

newt=spirala(t)
for i in range(9):
    print(newt[i])
