def gcd(a,b):

    if b==0:
        return a;
    else:
        a1=a%b
        return gcd(b,a1)


tok=[int(i) for i in input().split()]
print(gcd(max(tok),min(tok)))
