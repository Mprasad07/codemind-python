p,r,t=map(int,input().split())
n=p*(1+r/100)**t
print("{:.2f}".format(n))