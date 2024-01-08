def zad32(T,k,A,B,p=0):
    if k<1:
        if A==B: return True
    if p==len(T): return False
    return zad32(T,k-1,A+T[p],B,p+1) or \
    zad32(T,k-1,A,B+T[p],p+1) or \
    zad32(T,k,A,B,p+1)

print(zad32())
