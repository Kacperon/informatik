from math import log10
def czyzawiera(n):
    len=log10(n)//1 +1
    m=n
    while m>0:
        if m%10==len:
            return True
        m//=10
    return False
print(czyzawiera(12))