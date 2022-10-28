a,b=map(int,input().split())
p=a*b
while a!=0 and b!=0:
    if a>b:
        a%=b
    else:
        b%=a
gcd=b if a==0 else a
lcm=p//gcd
print(lcm)