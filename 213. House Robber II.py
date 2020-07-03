class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        
        a=False
        b=False 
        for i in range(2,len(nums)):
            if i%2==1: 
                if max(nums[:i-1])==nums[0]:
                    a=True
            else: 
                if max(nums[:i-1])==nums[0]:
                    b=True                
            nums[i]+=max(nums[:i-1])
        
        if a and : 
            nums[len(nums)-2]-=nums[0]
        if b: 
            nums[len(nums)-1]-=nums[0]

        print(nums)
        return max(nums[len(nums)-1],nums[len(nums)-2])



class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        a=[0]*(len(nums))
        n=nums[len(nums)-1]
        #a=False
        for i in range(2,len(nums)):
            if nums.index(max(nums[:i-1]))==0: 
                a[i]=1
            nums[i]+=max(nums[:i-1])
            a[i]=a[nums.index(max(nums[:i-1]))]

        if a[len(nums)-1]==0: 
            if nums[len(nums)-1]-nums[0]>nums[len(nums)-2]: 
                return nums[len(nums)-1]-nums[0]
            elif nums[len(nums)-1]-n>nums[len(nums)-2]:
                return nums[len(nums)-1]-n
            else: 
                return nums[len(nums)-2]
        else: 
            return  max(nums[len(nums)-1],nums[len(nums)-2])
    

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        #a=[0]*(len(nums))
        n=nums[len(nums)-1]
        a=False
        for i in range(2,len(nums)):
            if nums.index(max(nums[:i-1]))==2: 
                a=True
            nums[i]+=max(nums[:i-1])
            #a[i]=a[nums.index(max(nums[:i-1]))]

        if a: 
            if nums[len(nums)-1]-nums[0]>nums[len(nums)-2]: 
                return nums[len(nums)-1]-nums[0]
            elif nums[len(nums)-1]-n>nums[len(nums)-2]:
                return nums[len(nums)-1]-n
            else: 
                return nums[len(nums)-2]
        else: 
            return  max(nums[len(nums)-1],nums[len(nums)-2])
    

    class Solution:
    def rob(self, nums: List[int]) -> int:
    
        if nums==[]: 
            return 0
        
        if len(nums)==1: 
            return nums[0]       
        if len(nums)==3: 
            return max(nums[0],nums[1],nums[2])
        if len(nums)==4: 
            return max(nums[0]+nums[2], nums[1]+nums[3])
            
            
        #a=[0]*(len(nums))
        n=nums[len(nums)-1]
        a=False
        for i in range(2,len(nums)):
            if nums.index(max(nums[:i-1]))==2: 
                a=True
            nums[i]+=max(nums[:i-1])
            #a[i]=a[nums.index(max(nums[:i-1]))]

        if nums[0]==nums[1]: 
            a=False
        
        if a: 
            if nums[len(nums)-1]-nums[0]>nums[len(nums)-2]: 
                return nums[len(nums)-1]-nums[0]
            elif nums[len(nums)-1]-n>nums[len(nums)-2]:
                return nums[len(nums)-1]-n
            else: 
                return nums[len(nums)-2]
        else: 
            return  max(nums[len(nums)-1],nums[len(nums)-2])
    


#CORRECTED 

def robb(s,e,nums):
    arr=nums[s:e+1]
    if arr==[]: 
        return 0
    for i in range(2,len(arr)): 
        arr[i]+=max(arr[:i-1])
    return max(arr[len(arr)-1],arr[len(arr)-2])

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        if len(nums)==1: 
            return nums[0]
        return max(robb(0,len(nums)-2,nums),robb(1,len(nums)-1,nums))