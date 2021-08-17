def triple(n):
    if(n==2):
        return 1
    if(n==3):
        return 3
    s=triple(n-1)
    c=0
    for i in range (1,n):
        if(n%i==0):
            c+=1
        else:
            a=n%i
            if(i%a==0):
                c+=1
    return (s+c)            
t=int(input())
while t:
    n=int(input())
    print(triple(n))
    t-=1
    
