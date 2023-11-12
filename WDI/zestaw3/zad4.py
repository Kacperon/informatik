def zad4(n):
    e=[0 for _ in range(n+3)]
    epsi,epsi2=100,1000
    sil=1
    a=1
    
    while epsi>10:
        jeden=1
        for i in range(n):
            e[i]+=jeden//sil
            if e[i]>9:
                e[i]-=10
                e[i+1]+=1
            jeden*=10
            jeden//=sil
        a+=1
        sil*=a
        epsi=e[n]*100+e[n+1]*10+e[n+2]
        epsi=abs(epsi-epsi2)
        epsi2=epsi
    return e
print(zad4(10))