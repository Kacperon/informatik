def zad8(t):
    n=len(t)
    for i in range (n-2):
        q1=t[i][0]/t[i+1][1]
        q2=t[0][i]/t[1][i+1]
        count1,count2=True,True
        for j in range (1,n-i-1):
            if t[i+j][j]/t[i+j+1][j+1]!=q1:
                count1=False
            if t[j][i+j]/t[j+1][i+j+1]!=q2:
                count2=False
        if count1 or count2:
            return True,n-i
    return False,0
            

T1=[[1,2,3,6],
    [2,2,4,9],
    [5,7,4,9],
    [1,5,7,8]]
print(zad8(T1))