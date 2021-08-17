t=int(input())
while t:
    n,m=map(int,input().split(" "))
    d={}
    for i in range (m):
        a,b=map(int,input().split(" "))
        d[a]=b
    sorted_d = sorted(d.items(), key=lambda kv: kv[1])
    i=1
    while i<len(sorted_d):
        if(sorted_d[i-1][1]==sorted_d[i][1]):
            if(sorted_d[i-1][0]<=sorted_d[i][0]):
                del sorted_d[i-1]
            else:
                sorted_d[i]=sorted_d[i-1]
                del sorted_d[i-1]
        else:
            i+=1
    #print(sorted_d)        
    sorted_d.sort(reverse=True)
    #print(sorted_d)
    l=[0]*n
    for i in range (n):
        for j in range (len(sorted_d)):
            if((i+1)%(sorted_d[j][1])!=0):
                l[i]=sorted_d[j][0]
                break
    print(sum(l))        
    t-=1
