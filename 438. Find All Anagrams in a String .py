#Moving window 

#copy=copy(d)

def populate(p): 
    d=defaultdict(int)
    for  i in p: 
        d[i]+=1
    return d

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        #from copy import deepcopy
        #vec = deepcopy(v)
        d=defaultdict(int)
        
        #copy=defaultdict(int)
        ans=[]
        for  i in p: 
            d[i]+=1
            #copy[i]+=1
            
        #copy=deepcopy(d)
        
        i=0
        while i<len(s): 
            a=0
            print(d)
            print(s[i])
            #print(c)
            if s[i] in d: 
                d[s[i]]-=1
                if d[s[i]]==0: 
                    d.pop(s[i])
                    i+=1
                    a+=1
            else:
                d=populate(p)
                i-=a
                i+=1
                #d=copy
                
            if len(d)==0: 
                ans.append(i-len(p)+1)
                d=populate(p)
                #i-=a
                i+=1
        
        return ans
                
                
            
          

def check(i,j,d,s): 
    #print(s[i:j+1])
    for num in s[i:j+1]: 
        if num in d: 
            d[num]-=1
            if d[num]==0: 
                d.pop(num)
                if len(d)==0: 
                    return True
        else: 
            return False 
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        d=Counter(p)
        i=0
        j=i+len(p)-1
        while j<len(s): 
            if check(i,j,d,s):
                ans.append(i)
            d=defaultdict(int)
            d=Counter(p)
            j+=1
            i+=1
        return ans


def check(i,j,d,s): 
    #print(s[i:j+1])
    for num in s[i:j+1]: 
        if num in d: 
            d[num]-=1
            if d[num]==0: 
                d.pop(num)
                if len(d)==0: 
                    return True
        else: 
            return False 
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        d=Counter(p)
        i=0
        j=i+len(p)-1
        while j<len(s): 
            if check(i,j,d,s):
                ans.append(i)
            d=Counter(p)
            j+=1
            i+=1
        return ans


def check(i,j,d,s): 
    #print(s[i:j+1])
    
    if Counter(s[i:j+1])==d: 
        return True
    else: 
        return False
    
    """
    for num in s[i:j+1]: 
        if num in d: 
            d[num]-=1
            if d[num]==0: 
                d.pop(num)
                if len(d)==0: 
                    return True
        else: 
            return False 
    """

#Final edition 
    
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans=[]
        d=Counter(p)
        i=0
        j=i+len(p)-1
        while j<len(s): 
            if check(i,j,d,s):
                ans.append(i)
            #d=Counter(p)
            j+=1
            i+=1
        return ans