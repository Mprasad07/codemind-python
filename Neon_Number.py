n=int(input())
r=n*n
s=0
while r>0:
    t=r%10
    s=s+t
    r=r//10
if  s==n:
    print('Neon Number')
else:
    print('Not Neon Number')