

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        d=defaultdict(int) 
        for i in s: 
            d[i]+=1
            if d[i]==2: 
                d.pop(i)
        if not d: 
            return True 
        if len(d)==1: 
            for i in d: 
                if d[i]==1: 
                    return True
        else: 
            return False 
        