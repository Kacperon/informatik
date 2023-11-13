from random import randint

def czy_uro(n):
    tab=[randint(1,365) for _ in range(n)]
    tab_ilo=[0 for _ in range(365)]
    for i in range(n):
        tab_ilo[tab[i]-1]+=1
        if tab_ilo[tab[i]-1]>1:
            return True
    return False
def zad14():
    praw=[0 for _ in range(21)]
    pr=100000
    for i in range(20,41):
        licznik=0
        for j in range(pr):
            if czy_uro(i):
                licznik+=1
        praw[i-20]=licznik/pr
    return praw
print(zad14())

