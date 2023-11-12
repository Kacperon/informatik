from math import log10
def czy_zl_nieparzyste(liczba):
    n=int(log10(liczba)+1)
    for i in range (n):
        ostatnia=liczba%10
        liczba//=10
        if ostatnia%2==0:
            return False
    return True
def zad2(t):
    n=len(t)
    for w in range(n):
        wiersz=False
        for k in range(n):
            if czy_zl_nieparzyste(t[w][k]):
                wiersz=True
        if not wiersz:
            return False
    return True

tab=[[41,2],[311597,8]]
print(zad2(tab))