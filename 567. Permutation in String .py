class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        
        d=Counter(s1)
        i=0
        j=i+len(s1)-1
        while j<len(s2): 
            if Counter(s2[i:j+1])==d: 
                return True
            j+=1 
            i+=1
        return False
                