class Solution:
    def numSquares(self, n: int) -> int:
        if n==1: 
            return 1
        d=[float("inf")]*(n+1)
        l=[]
        d[0]=0
        ni=n
        #print(ni)
        for i in range(1,ni): 
            l.append(i**2)
        for x in l: 
            for c in range(x, n+1): 
                d[c]=min(d[c],d[c-x]+1)
        
        return d[n] 
        #print(ni)
