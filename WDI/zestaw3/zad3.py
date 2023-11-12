def sito(n):
    if n<=1:
        return []
    t=[True for _ in range (n)]
    t[0],t[1]=False,False
    for i in range (4,n,2):
        t[i]=False
    d=3
    while d<= n**0.5:
        if t[d]:
            for i in range(2*d,n,d):
                t[i]=False
        d+=2

    ilosc=0
    for i in range (n):
        if t[i]:
            ilosc+=1
    pierwsze=[0 for _ in range(ilosc)]
    inde_pierw=0
    for i in range(n):
        if t[i]:
            pierwsze[inde_pierw]=i
            inde_pierw+=1

    return pierwsze
    # with open('a.py','w') as f:
    #     f.write("t=")
    #     f.write(str(pierwsze))   
print (sito(6))




# def sito2_0(n):
#     t=[True]*n
#     t[0],t[1]=False,False
#     for i in range (4,n,2):
#         t[i]=False
#     for i in range (9,n,6):
#         t[i]=False
#     # for i in range (25,n,10):
#     #     t[i]=False
#     # for i in range 
#     pierwsze=[]
#     for i in range (n):
#         if t[i]:
#             pierwsze.append(i)
#     return pierwsze
