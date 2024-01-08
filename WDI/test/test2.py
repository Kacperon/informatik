def dzial(n):
    wynik=(n**3-1)/(n**3+1)
    return wynik
def wynik(n):
    iloczyn=1
    for i in range (2,1+n):
        iloczyn*=dzial(i)
    return iloczyn
print(wynik(10000000))