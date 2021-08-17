t=int(input())
while t:
    k=int(input())
    l=[]
    if k==2:
        print(23)
    else:
        for i in range (1,k+1):
            l.append(i)
        print(*l,sep='')
    t-=1            
