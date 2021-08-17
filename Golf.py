t=int(input())
while t:
    n,x,k=map(int,(input().split(" ")))
    if n+1%k==0:
        if (x%k==0):
            print("YES")
        else:
            print("NO")
    else:
        if(x%k==0):
            print("YES")
        else:
            a=n+1-x
            if a%k==0:
                print("YES")
            else:
                print("NO")
    t-=1
