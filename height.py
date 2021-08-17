class Solution:
    def getMinDiff(self, arr, n, k):
        # code here
        a=min(arr)
        b=max(arr)
        if b-k<=0:
            b+=k
        else:
            b-=k
        if a-k<=0:
            a+=k
        else:
            a-=k
        return b-a;        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        k = int(input())
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.getMinDiff(arr, n, k)
        print(ans)
        tc -= 1
