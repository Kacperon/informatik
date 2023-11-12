def sumel(n):
    sum=0
    a,b=1,1
    while sum<n:
        sum+=a
        a,b=b,a+b
    a,b=1,1
    while sum>n:
        sum2=sum
        sum-=a
        a,b=b,a+b
    if sum==n:
            return(sum)
    return(sum2)
print(sumel(12))