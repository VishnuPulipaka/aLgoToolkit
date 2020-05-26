def gcd(a,b):
    if b==0:
        return a;
    else:
        a1=a%b
        return gcd(b,a1)


def lcm(a,b):
     out=(a*b)/gcd(a,b)
     return int(out)

k=[int(i) for i in input().split()]
print(lcm(k[0],k[1]))
