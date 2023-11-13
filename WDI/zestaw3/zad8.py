from random import randint
n=10**5
T=[randint(10,20) for _ in range(n)]

def zad8(t):
    n=len(t)
    t_droga=[False for _ in range(n)]
    t_droga[0]=True
    for i in range(n):
        if t_droga[i]:
            kopia=t[i]
            czynnik=2
            while kopia>1:
                while kopia%czynnik==0:
                    kopia//=czynnik
                    if i+czynnik<n:
                        t_droga[i+czynnik]=True
                czynnik+=1
    print(t,"\n",t_droga)
    return t_droga[n-1]

print(zad8(T))
                

            
