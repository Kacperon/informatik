def czywiel(n):
    an=2
    while an<=n:
        zap=an
        while zap<=n:
            if zap==n:
                return True
            zap+=zap 
        an=3*an+1  
    return(False)
print(czywiel(7))