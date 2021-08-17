import math
def find_gcd(x, y):
    while(y):
        x, y = y, x % y
  
    return x
def sumnum(a):
     b=0
     for i in a:
         b+=i
     return b    
def gcd(A):
    num1=A[0]
    num2=A[1]
    gc=find_gcd(num1,num2)
    for i in range (2,len(A)):
         gc=find_gcd(gc,A[i])
    return gc     
t=int(input())
while t:
    n=int(input())
    l=list(map(int,input().split(" ")))
    l.sort()
    a=l[0]
    count=0
    l1=[]
    for i in l:
        if i%a!=0:
            count+=1
    if count==0:
        l[n-1]=a
        sum=0
        for i in l:
            sum+=i//a
        print(sum)    
    elif count==1:
        sum=0
        for i in l:
            if i%a!=0:
                i=a
            sum+=i//a
        print(sum)    
    else:
        l1=l[1::]
        if(gcd(l1)==1):
            su=sumnum(l)
            su=(su-max(l))+1
            print(su)
        else:
            l[0]=gcd(l1)
            a=l[0]
            sum=0
            print(l)
            for i in l:
                sum+=i//a
            print(sum)    
    t-=1
