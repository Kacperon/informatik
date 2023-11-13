from random import randint
n=5
T=[randint(1,1000) for _ in range(n)]
def zad6(T):
    n=len(T)
    for i in range(n):
        liczba=T[i]
        flaga=False
        while liczba>0:
            if liczba%2==1:
                flaga=True
            liczba//=10
        if not flaga:
            return False
    return True
print(zad6(T))