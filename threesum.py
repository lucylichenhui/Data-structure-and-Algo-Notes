

#Did not solve the 2 largest test cases

from collections import defaultdict
def threeSum(nums):
    sol=[]
    nums.sort()
    d=defaultdict(list)
    i=0
    for e in nums: 
        d[e].append(i)
        i+=1

    for i in range(len(nums)): 
        j=i+1
        while j<len(nums):
            curr=0-nums[j]-nums[i]
            
            if curr in d: 
                if j not in d[curr] and i not in d[curr]:

                        stack=set()
                        stack.add(curr)
                        stack.add(nums[j])
                        stack.add(nums[i])
                        mini=min(curr, nums[j],nums[i])
                        stack.remove(mini)
                        maxi=max(curr, nums[j],nums[i])
                        stack.remove(maxi)
                        for e in stack: 
                            ii=e
                            if [mini,ii,maxi] not in sol: 
                                sol.append([mini,ii,maxi])

                elif j in d[curr] and i not in d[curr]: 
                    #print(d[curr])
                    s=set() 
                    for element in d[curr]: 
                        if element!=j:
                            l=[curr, nums[j],nums[i]]
                            l.sort()
                            if l not in sol: 
                                sol.append(l)
                elif i in d[curr] and j not in d[curr]: 
                    #print(d[curr])
                    s=set() 
                    for element in d[curr]: 
                        if element!=i:
                            l=[curr, nums[j],nums[i]]
                            l.sort()
                            if l not in sol: 
                                sol.append(l)


                elif j in d[curr] and i in d[curr]: 
                    #print(d[curr])
                    s=set() 
                    for element in d[curr]: 
                        if element!=i and element!=j:
                            l=[curr, nums[j],nums[i]]
                            l.sort()
                            if l not in sol: 
                                sol.append(l)
            j+=1
    return sol

        
threeSum([-1,0,1,2,-1,-4])
#print(sol)
        

##########

#official solution 

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        found = set()
        for i, val1 in enumerate(nums):
            seen = set()
            for j, val2 in enumerate(nums[i+1:]):
                complement = -val1 - val2
                if complement in seen:
                    min_val = min((val1, val2, complement))
                    max_val = max((val1, val2, complement))
                    if (min_val, max_val) not in found:
                        found.add((min_val, max_val))
                        res.append([val1, val2, complement])
                seen.add(val2)
        return res


