t=int(input())
while t:
    a,b,c=map(int,input().split(" "))
    d=b+(100-a)*c
    print(d*10)
    t-=1
