def isprime(n):
    a=0
    for i in range (2,n-1):
        if n%i==0:
            a=1
    if a==1:
        return False
    else:
        return True
            
def digit(n):
    su=0
    for i in str(n):
        su+=int(i)   
    return su   
def sumnumber(a):
    li=[]
    for i in range(a):
        if isprime(i):
            li.append(i)
    n=sum(li)-1
    #print(n)
    a=digit(n)
    return a
s=input()
count=0
for i in s:
    if i=='a' or i=='e' or i=='o' or i=='u' or i=='i':
        a=count*100
        b=sumnumber(a)
        #print(b)
        if b>9:
            b=digit(b)
        c=str(b)
        s=s.replace(i,c,1)
    count+=1    
print(s)        
