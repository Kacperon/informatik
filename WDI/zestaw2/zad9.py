def pole(k,n):
    i,pole=1,0
    while i<k:
        pole+=1/i*n
        i+=n
    return(pole)
print(pole(2,0.001))
