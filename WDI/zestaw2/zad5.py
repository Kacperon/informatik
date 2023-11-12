from math import log10
def ilepodz7(n):
    ilosc=0
    ilosccyfr=int(log10(n))+1
    for i in range(1,2**ilosccyfr):
        pot=0
        wynik,m,j=0,n,i
        while m>0:
            if j%2:
                wynik+=m%10*10**pot
                pot+=1
            j//=2
            m//=10
        if not wynik%7:
           print(wynik)
           ilosc+=1
    return(ilosc)
print(ilepodz7(2317))              
