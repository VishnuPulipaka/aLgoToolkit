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


def fibo(n):
    n=n%60

    sum=0
    dig=pisanoPeriod(10)
    for i in range(n+1):
        sum=sum+dig[i]**2
    
    return sum%10

k=int(input())
print(fibo(k))
