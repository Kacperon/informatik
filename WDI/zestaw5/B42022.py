T=[[False,True,False,False,True],
   [False,False,False,True,False],
   [True,False,False,False,False],
   [False,False,False,False,False],
   [False,True,False,False,False]]
def czy_brakuje_jednej(t):
    n=len(t)
    ilosc=1
    for i in range(n):
        if t[i]:
            ilosc+=1
    if ilosc==n:
        return True
    return False
def zad2(t):
    n=len(t)
    wie=[0 for _ in range(n)]
    for w in range(n):
        for k in range(n):
            if t[w][k]:
                wie[w]+=1
    if czy_brakuje_jednej(wie):
        w=0
        while wie[w]<2:
            w+=1
        k=0
        while not t[w][k]:
            k+=1
        w2=0
        while wie[w2]:
            w2+=1
        return w,k,w2,0
    wie=[0 for _ in range(n)]
    for k in range(n):
        for w in range(n):
            if t[w][k]:
                wie[k]+=1
    if czy_brakuje_jednej(wie):
        k=0
        while wie[k]<2:
            k+=1
        w=0
        while not t[w][k]:
            w+=1
        k2=0
        while wie[k2]:
            k2+=1
        return w,k,0,k2
print(zad2(T))