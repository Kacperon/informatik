def zad2(num1,num2):
    tab=[0 for _ in range(10)]
    while num1>0:
        i=num1%10
        tab[i]+=1
        num1//=10
    while num2>0:
        i=num2%10
        tab[i]-=1
        num2//=10
    for i in range(10):
        if tab[i]!=0:
            return False
    return True
print(zad2(1234,4321))