# def ejest(x):

#     e=(1+1/x)**x
#     return e
# print(ejest(100000000000000))
# def coś():
#     return 1>0
# print(coś())
# #siema ja fan

# def NWD(a,b):
#     while b!=0:
#         a,b=b,a%b
#     return a
# print(NWD(242,44))
# a=123456789
# t=[]
# for i in str(a):
#     t+=[i]
# print(str(a)[10])

def waga(n):
    wagens=0
    if n<=1:
        return 0
    else:
        flag=0
        i=2
        while i*i<=n:
            print(i,n)
            if n%i==0:
                if flag==0:
                    wagens+=1
                flag=1
                n=n//i
            else:
                flag=0
                i+=1
        if n != 1:
            wagens += 1
        return wagens
    
print(waga(65))

print(ord('A'))