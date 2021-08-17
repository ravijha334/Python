t=int(input())
while t:
    a,b=map(int,input().split(" "))
    s=input()
    l=list(s)
    count=0
    c=0
    for i in range (len(l)):
        if l[i]=="*":
            count+=1
        if l[i]!="*":
            count=0
        if(count==b):
            c=1
    if c==1:
        print("YES")
    else:
        print("NO")
    t-=1
