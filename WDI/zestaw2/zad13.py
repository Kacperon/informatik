def czzyzakonczona(n):
    m=n
    cyfra=m%10
    m//=10
    while m>0:
        if m%10==cyfra:
            return False
        m//=10
    return True
print(czzyzakonczona(145556762))
