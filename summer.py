t=int(input())
while t:
    a,b,a1,b1=map(int,input().split(" "))
    c=a1//a
    d=b1//b
    print(c+d)
    t-=1
