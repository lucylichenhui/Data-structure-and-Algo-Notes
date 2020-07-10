class Solution:
    def integerBreak(self, n: int) -> int:
        d=[float(0)]*(n+1)
        if n==1: 
            return 0
        if n==2: 
            return 1 
        if n==3: 
            return 2
        if n==4: 
            return 4 
        d[0]=0
        d[1]=1
        d[2]=2
        d[3]=3
        d[4]=4
        for i in range(4,n+1): 
            m=0
            for j in range(i): 
                m=max(d[j]*d[i-j],m)
                d[i]=max(d[j]*d[i-j],m)
        return d[n]
                
