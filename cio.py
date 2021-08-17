t=int(input())
while t:
    c,d,p,q=map(int,input().split(" "))
    a=c//d
    l=a
    b=c%d
    a-=1
    su=p*c
    snat=(a*(a+1))//2
    su=su+(q*d*snat)
    if b==0:
        print(su)
    else:
        su=su+(b*l*q)
        print(su)
    t-=1
