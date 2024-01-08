#Na szachownicy o wymiarach N ×N wypełnionej liczbami naturalnymi > 1 odbywają się wyścigi
#wież. Pierwsza wieża startuje z lewego górnego rogu i ma dotrzeć do prawego dolnego rogu szachownicy. Pierwsza wieża może wykonywać tylko ruchy w prawo lub w dół szachownicy. Druga wieża
#startuje z prawego górnego rogu i ma dotrzeć do lewego dolnego rogu szachownicy. Druga wieża
#może wykonywać tylko ruchy w lewo lub w dół szachownicy. Wygrywa wieża, która dotrze do mety
#w mniejszej liczbie ruchów. Wieże mogą wykonać ruch z jednego pola na drugie tylko wtedy, gdy
#liczby na obu polach są względnie pierwsze.
#Proszę napisać funkcję, która dla danej tablicy zwraca numer wieży, która wygra wyścig lub 0, jeżeli
#wyścig będzie nierozstrzygnięty. Można założyć, że podczas wyścigu wieże nie spotkają się na jednym
#polu. Po wykonaniu funkcji zawartość tablicy nie może ulec zmianie.
def czy_wzgl_pierw(a,b):
    while b!=0:
        a,b=b,a%b
    return a==1
def obrot(t):
    n=len(t)
    t2=[[0 for _ in range(n)] for _ in range(n)]
    for w in range(n):
        for k in range(n):
            t2[w][k]=t[w][n-k-1] # t[n-k-1][w]
    return t2
def zad3(t):
    n=len(t)
    minlicz=10**10
    t2=obrot(t)
    def ruchy(t,w,k,n,licznik):
        nonlocal minlicz
        if w==n-1 and k==n-1:
            minlicz=min(minlicz,licznik)
        if w<n:
            for i in range(w+1,n):
                if czy_wzgl_pierw(t[w][k],t[i][k]):
                    ruchy(t,i,k,n,licznik+1)
        if k<n:
            for i in range(k+1,n):
                if czy_wzgl_pierw(t[w][k],t[w][i]):
                    ruchy(t,w,i,n,licznik+1)
        return minlicz
    ruchy1=ruchy(t,0,0,n,0)
    ruchy2=ruchy(t2,0,0,n,0)
    print(ruchy1,ruchy2)
    if ruchy1==ruchy2:
        return 0
    elif ruchy1<ruchy2:
        return 1
    else: return 2
t=[[123, 15, 15, 15, 2],
[21, 4, 10, 4, 2],
[3, 3, 7, 10, 10],
[10, 10, 6, 3, 3],
[3, 7, 3, 6, 15]]

print(zad3(t))


