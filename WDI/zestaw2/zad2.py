def dziel(a,b,n):
    wynik=a//b
    print(wynik,end=',')
    for i in range(n):
        a=a%b
        a*=10
        wynik=a//b
        print(wynik,end='')
        foo=0
    print()

       
dziel(60,2,10)
