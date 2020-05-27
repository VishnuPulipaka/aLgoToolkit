def pisanoPeriod(m):
    dig=[0,1]
    a=0
    b=1
    prev=0
    cur=1
    for i in range(0,m*m):
        c=a+b
        prev=cur
        cur=c%m

        a=b
        b=c
        if cur==1 and prev==0:
            return dig[:-1]
        dig.append(cur)


def fibo(m,n):
    n=n%60
    m=m%60
    sum=0
    dig=pisanoPeriod(10)
    for i in range(m,n+1):
        sum=sum+dig[i]

    return sum%10

'''def fibo(m,n):
    n=n%60
    m=m%60
    a=0
    b=1
    sum=0
    sum1=0
    if n<=2 and m<=2:
        return n-m
    elif m<=1 and n>1:
        a=0
        b=1
        sum1=m;
        sum=0;
        for k in range(n-1):
            c=a+b
            a=b
            b=c
            sum=sum+c
        return (sum-sum1)%10
    else:
        a=0
        b=1
        sum1=0;
        for k in range(m-2):
            c=a+b
            a=b
            b=c
            sum1=sum1+c

        a=0
        b=1
        sum=0;
        for k in range(n-1):
            c=a+b
            a=b
            b=c
            sum=sum+c
        return (sum-sum1)%10'''

k=[int(i) for i in input().split()]
print(fibo(k[0],k[1]))
