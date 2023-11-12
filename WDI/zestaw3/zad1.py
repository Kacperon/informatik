
def zad1(num):
    tab=[0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
    for i in range(2,17):
        numzap=num
        wynik=str()
        while numzap>0:
            wynik+=str(tab[numzap%i])
            numzap//=i
        print(wynik[::-1], end=", ")
zad1(15)
