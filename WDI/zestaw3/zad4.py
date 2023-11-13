def zad4(n):
    e=[0 for _ in range(n)]
    
    epsi,epsi2=1000,1000
    silnia=1
    # while epsi>10:
    for i in range(1,n):
        jedynka=1
        for j in range(n):
            if silnia>10**n:
                break
            e[j]+=jedynka//silnia
            if e[j]>9:
                e[j-1]+=1
                e[j]-=10
            jedynka%=silnia
            jedynka*=10
        silnia*=i
    return e
def printe(T):
    print(T[0],end='')
    print('.',end='')
    for i in range(1,len(T)):
        print(T[i],end='')
    print()
printe(zad4(3000))
#2.7182818284590455
#54688957034808
#54688957034808