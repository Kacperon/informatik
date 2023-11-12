def czy_zgodne(a,b):
    sum=0
    while a>0:
        sum+=a%2
        a//=2
    while b>0:
        sum-=b%2
        b//=2
    return sum==0
def zad14(t1,t2):
    n1,n2=len(t1),len(t2)
    procent=n1**2
    for w2 in range (0,n2-n1+1):
        for k2 in range (0,n2-n1+1):
            licz=0
            for w1 in range (n1):
                for k1 in range (n1):
                    if czy_zgodne(t1[w1][k1],t2[w2+w1][k2+k1]):
                        licz+=1
            if licz/procent>0.33:
                return True
    return False


T2 = [
    [22, 52, 7, 8],
    [24, 109, 6, 7],
    [12, 14, 17, 18],
    [9, 9, 4, 4]]

T1 = [
    [101, 101],
    [101, 101]
]
print(zad14(T1,T2))

