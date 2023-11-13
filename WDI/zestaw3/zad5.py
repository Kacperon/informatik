def zad5():
    i=int(input(":"))
    t=[0 for _ in range(10)]
    while i!=0:
        for j in range(10):
            if t[j]<=i:
                for k in range(9,j,-1):
                    t[k]=t[k-1]
                t[j]=i
                break
        i=int(input(":"))
    print(t)
    return t[9]
print(zad5())

