def check(s,i,j,wordDict): 
    global B
    
    for item in wordDict: 
        if item==s[i:j+1]:
            return True
  
    return False


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if len(s)==1: 
            if s in wordDict: 
                return True
            else: 
                return False
        i,j=0,0
        B=False
        while j<len(s):
            if check(s,i,j,wordDict):
                B=True
                i+=len(s[i:j+1])
                j=i
                print(j)
                if j>len(s)-1: 
                    break
            else: 
                B=False
                j+=1
                if j>len(s)-1: 
                    break
                    
        
        if not B: 
            return False

        else: 
            return True  

#Correction

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp=[False]*(len(s)+1)
        dp[0]=True
        for i in range(1,len(s)+1): 
            for j in range(i): 
                if dp[j] and s[j:i] in wordDict: 
                    dp[i]=True
                    break 
        
        return dp[len(s)]