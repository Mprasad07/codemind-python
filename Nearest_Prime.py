tt=int(input())
for _ in range(tt):
    x=int(input())
    np=x
    while True:
        is_prime=True
        for i in range(2,int(np**0.5)+1):
            if np%i==0:
                is_prime=False
                break
        if is_prime==True:
            break
        np+=1
    pp=x
    while True:
        fc=0
        for i in range(1,pp+1):
            if pp%i==0:
                fc+=1
        if fc==2:
            break
        pp-=1
    if x-pp<=np-x:
        print(pp)
    else:
        print(np)