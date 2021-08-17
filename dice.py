t=int(input())
while t:
    n=int(input())
    sm=(n//4)*44
    rem=n%4
    if (n>=4):
        if rem==0:
            sm+=16
        if rem==1:
            sm+=32
        if rem==2:
            sm+=44
        if rem==3:
            sm+=55
        print(sm)
    else:
        if n==1:
            print(20)
        if n==2:
            print(36)
        if n==3:
            print(51)
    t-=1






