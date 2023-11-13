T=[2,9,3,1,7,11,9,6,7,7,1,3,9,12,15]
def zad13(t):
    n=len(t)
    i=0
    liczmax=0

    for i in range(n):
        for j in range(n-1,i,-1):
            licznik=0
            if t[i]==t[j]:
                licznik+=1
                while t[i+1]==t[j-1]:
                    licznik+=1
                    i+=1
                    j-=1
            if liczmax<licznik:
                liczmax=licznik
    return liczmax
print(zad13(T))

                