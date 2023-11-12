def czywiel(n):
    i=0
    an=1
    while an<=n:
        an=i*i+i+1
        while an<=n:
            if an==n:
                return True
            an+=an
        an=1
        i+=1
    return(False)
print(czywiel(999))