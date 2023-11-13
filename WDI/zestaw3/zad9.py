from random import randint
n=10**7
T=[randint(1,1000) for _ in range(n)]
def zad9(t):
    n=len(t)
    liczmax=1
    licznik=1
    for i in range(n-1):
        
        if t[i]<t[i+1]:
            licznik+=1
        else:
            if liczmax<licznik:
                liczmax=licznik
            licznik=1   
    return liczmax
print(zad9(T))
