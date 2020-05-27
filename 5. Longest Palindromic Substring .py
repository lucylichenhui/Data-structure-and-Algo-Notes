


def checkifp(s): 
    if s[::-1]==s: 
        return True #len(s)
    else: 
        return False
    
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s =="": 
            return ""
        if len(s)==1:
            return s
        if len(s)==2: 
            if s[1]!=s[0]: 
                return s[0]
            else: 
                return s
        length=0
        sol=[]
        for i in range(1,len(s)-1):
            n=0
            #odd
            if i-n>0 or i+n+1<len(s): 
                while checkifp(s[i-n:i+n+1]) is True:
                    
                    #print(s[i-n:i+n+1])
                    if i-n>0 or i+n+1<len(s): 
                        n+=1
                        if i-n<0 or i+n+1>=len(s): 
                            break
            #print(i,n)
                    #print(i-n)
                    #print(i+n)
            if 2*n-1>length: 
                #print(2*n+1)
                length=2*n-1
                sol=s[i-n:i+n+1]
                print(sol)
        for i in range(0,len(s)-1): 
            n=0
            #even
            if i-n>0 or i+n<len(s): 
                while checkifp(s[i-n:i+n]) is True: 
                    n+=1 
                    if i-n<0 or i+n>=len(s): 
                        break
            if n*2>length: 
                length=n*2
                sol=s[i-n+1:i+n-1]
        return sol


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        ln = len(s)
        maxlen = 0
        for i in range(ln):
            for j in range(i,ln):
                op = s[i] + s[i+1:j+1]
                # print(op)
                if op == op[::-1]:
                    if len(op) > maxlen:
                        maxlen = len(op)
                        result = op
        return result


class Solution:
    def longestPalindrome(self, s: str) -> str:
        self.max_length, self.ret = 0, ""
        
        def expand(left, right):
            while left > 0 and right < len(s) - 1:
                if s[left-1] == s[right+1]:
                    left -= 1
                    right += 1
                else:
                    break
            if right - left + 1 > self.max_length:
                self.max_length = right - left + 1
                self.ret = s[left: right+1]
        
        for i in range(len(s)):
            expand(i, i)
            if i + 1 < len(s) and s[i] == s[i+1]:
                expand(i, i+1)
        return self.ret