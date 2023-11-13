from random import randint
n=10**2
T=[1,2,4,6,8,10,12,14,16,18,20,30]
def zad10(t):
    n=len(t)
    r=t[0]-t[1]
    licznik=1
    liczmax=1
    for i in range(n-1):
        if r==t[i]-t[i+1]:
            licznik+=1
        else:
            if liczmax<licznik:
                liczmax=licznik
            licznik=1
            r=t[i]-t[i+1]
    print(t)
    return liczmax
print(zad10(T))

