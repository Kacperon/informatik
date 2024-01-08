
def rurociag(T,S):
    min=10**10
    def reku(t,s,i=0,suma=0,ilosc=0):
        nonlocal min
        if suma==s and ilosc<min:
            min=ilosc
        if i<len(t):
            reku(t,s,i+1,suma+t[i],ilosc+1)
            reku(t,s,i+1,suma,ilosc)
        return min
    return reku(T,S)
T=[2,7,4,3,11]
suma=16
print(rurociag(T,suma))

