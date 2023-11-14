T1=[8,13,17,19,23,2,6,4,8,3,5,7,1,3,2] 
T2=[]
def zad(t):
    n=len(t)
    i=0
    tmaxmax,tminmin=10**10,0
    while i<n-1:
        flag=1
        tmin=t[i]
        while t[i]<t[i+1]:
            tmax=t[i+1]
            i+=1
            flag+=1
        if flag>2:
            if tmin>tminmin:
                tminmin=tmin
            if tmax<tmaxmax:
                tmaxmax=tmax
        i+=1
    if tminmin>tmaxmax:
        return True
    return False
print(zad(T1))