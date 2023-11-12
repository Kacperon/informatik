def zad6(t1):
    n=len(t1)
    t2=[0 for _ in range(n*n)]
    liczt2=-1
    wykorzystane=[0 for _ in range (n)]
    for i in range(n*n):
        max=0
        for w in range(n):
            if wykorzystane[w]<n:
                liczba=t1[w][n-1-wykorzystane[w]]
                if liczba>max:
                    max=liczba
                    w_wybrany=w
        if t2[liczt2]!=max:
            liczt2+=1
            t2[liczt2]=max
        wykorzystane[w_wybrany]+=1
    return t2


T1=[[1,2,3,6],
    [2,2,2,9],
    [5,7,8,10],
    [1,5,7,15]]
print(zad6(T1))