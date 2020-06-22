class Solution:
    def longestPalindrome(self, s: str) -> int:
        
        d=defaultdict(int)
        cnt=0
        for i in s: 
            d[i]+=1
            if d[i]==2: 
                d.pop(i)
                cnt+=2
                
        if len(s)>cnt:        
            return cnt+1
        else: 
            return cnt
        