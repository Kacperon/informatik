def czyros(n):
    while n>0:
        a=n%10
        b=n%100
        b//=10
        if b>=a:
            return(False)
        n//=10
    return(True)
print(czyros(23567899))