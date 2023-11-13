def e(n):
    silnia=1
    suma=0
    for i in range (1,n):
        suma+=1/silnia
        silnia*=i
    return suma

def silnia(n):
    silnia=1
    for i in range(2,n+1):
        silnia*=i
    return silnia
print(len(str(silnia(1000))))
def sprawdz(n):
    silnia=1
    i=1
    while silnia<10**n:
        silnia*=i
        i+=1
    return i
print(sprawdz(100))


