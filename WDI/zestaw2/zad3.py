from math import log10
def czypali(n):
    m=n
    wynik=0
    for i in range (int(log10(n))+1):
        wynik+=m%10
        wynik*=10
        m//=10
    wynik/=10
    return wynik==n
    
print(czypali(100001))

