m=(10**9)+7
a=[]
for i in range (1,1000003):
    s=(2**i)%m
    a.append(s)
t=int(input())
print(a)
while t:
    a,b=map(int,input().split(" "))
    x=a[n]-1
    y=b
    temp=1
    while(y>0):
        if y%2==1:
            temp=(x*temp)%m
        x=x*x
        y=y//2
    print(temp)
    t-=1
