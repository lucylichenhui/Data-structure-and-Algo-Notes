
#Q 168. Given a positive integer, return its corresponding column title as appear in an Excel sheet.


def numbertotitle(n): 
    d=dict(zip(range(1,27),string.ascii_uppercase))    
    s=""
    while n!=0: 
        if n%26==0: 
            s+="Z"
            n=n/26 
            n-=1 
        else: 
            r=n%26 
            s+=d[r]
            n-=r 
            if n!=0:
                n=n/26
    s=s[::-1]
    return s

#better solution
def convertToTitle(self, n: int) -> str:
    ans = ""
    while n > 0:
        n, b = divmod(n - 1, 26)
        ans += (chr(ord('A') + b))
    return ans[::-1]

#Q 171. Given a column title as appear in an Excel sheet, return its corresponding column number.

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        k=[]
        d=dict(zip(string.ascii_uppercase,range(1,27)))    
        num=0
        i=0
        while i<len(s): 
            num+=(d[s[i]])*26**(len(s)-1-i)
            i+=1
        return num