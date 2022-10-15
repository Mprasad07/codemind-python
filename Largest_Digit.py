n=int(input())
id=0
while n>0:
    r=n%10
    if r>id:
        id=r
    n=n//10
print(id)