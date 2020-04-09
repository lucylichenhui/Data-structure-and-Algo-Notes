
# wrong utility function, enumerate returns index for position of char in string 
# not the freq of char in string

# you did not read the ques carefully at first 
def checkstring(l): 
        for i in enumerate(l): 
            print(i)
        for c,e in enumerate(l): 
        if c<=1:
            print(l)
            return True 
            

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
    final=[]
    for i in range(len(s)): 
        j=i+1
        while j<len(s)-i: 
            l=s[i,j]
            if checkstring(l): 
                ans=l
                final.append(ans,j-i)
                j+=1
            else: 
                break

    sum=0
    for val in final: 
        if val[1]>sum:
            sol=val[0]
            sum=val[1]
    return sol
def checkstring(l): 
    #collections.Counter(s).most_common(1)[0]
    d={}
    for i in l:         
        if i in d:
            if d[i]<1: 
                d[i]+=1 
            else: 
                return False
        else: 
            d[i]=1
    return True 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": 
            return 0
        final=[]
        finalans=[]
        for i in range(len(s)): 
            #print(i)
            j=i+1
            while j<len(s)+1: 
                l=s[i:j]
                #print(l)
                if checkstring(l): 
                    ans=j-i
                    finalans.append(ans)
                    j+=1
                else: 
                    break
        if finalans:
            sol=max(finalans)
        else: 
            sol=1
        return sol


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
		if len(s)<=1:
            return len(s)
        
		start,pos,res=0,{},0
      
        for i,x in enumerate(s):
            if x in pos and pos[x]>=start:
                res=max(res,i-start)
                start=pos[x]+1
            pos[x]=i
        
        return max(res,len(s)-start)







def checkstring(l): 
    #collections.Counter(s).most_common(1)[0]
    d=set()
    for i in l:         
        if i in d:
            return False
        else: 
            d.add(i)
    return True 

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s == "": 
            return 0
        final=[]
        finalans=[]
        for i in range(len(s)): 
            #print(i)
            j=i+1
            while j<len(s)+1: 
                l=s[i:j]
                #print(l)
                if checkstring(l): 
                    ans=j-i
                    finalans.append(ans)
                    j+=1
                else: 
                    break
        if finalans:
            sol=max(finalans)
        else: 
            sol=1
        return sol
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_longest, c_ix = 0, 0
        un = []
    
        if len(s) == 0: # edge case
            return 0
    
        for s in s:
            if s not in un: # if we haven't seen a given letter, let's add it to the list 'un'
                un.append(s)
                max_longest = max(max_longest, len(un)) # keep the length of the longest chain that we came across so far
            else: # if we bump into a letter that we've already seen 
# reshape our list: un.index(s) - it's the index of the element that we've already seen
# plus one moves us to the next element, while ':' to the end of the list
# + [s] takes this repetitive element and puts it to the end of the list. Thus, we make a sliding step and reshaped the list 'un' 
                un = un[un.index(s)+1:] + [s]
        return max_longest