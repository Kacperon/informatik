def fib (n):
    a,b=1,1
    for i in range (n):
        a,b=b,a+b
    return a
def ilfib (n):
    i,j=1,1
    iloczyn=1
    while iloczyn<=n:
        iloczyn=fib(i)
        liczba=1
        while liczba<=n:
            liczba=iloczyn*fib(j)
            j+=1
            if liczba==n:
                return(True)
        j=1
        i+=1

    return(False)

print(ilfib(1155))
        