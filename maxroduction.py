t=int(input())
while(t):
    d,x,y,z=map(int,input().split(" "))
    a=7*x
    c=7-d
    b=(d*y)+(c*z)
    print(max(a,b))
    t-=1
