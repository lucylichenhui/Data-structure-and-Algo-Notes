class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        s=[]
        for i in S: 
            if i!="#": 
                s.append(i)
            else: 
                if len(s)>0:
                    s.pop()
        t=[]
        for i in T: 
            if i!="#": 
                t.append(i)
            else: 
                if len(t)>0:
                    t.pop()
        if t==s: 
            return True 
        else: 
            return False