
def minroz(n):
    sqr=(n**0.5)//1
    while n>=sqr:
        if n%sqr==0:
            return(sqr,n/sqr)
        sqr+=1
print(minroz(120))

