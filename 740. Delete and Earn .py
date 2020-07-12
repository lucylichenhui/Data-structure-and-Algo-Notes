class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        
        if len(nums)==1:
            return nums[-1]
        arr=(max(nums)+1)*[0]
        nums.sort()
        print(nums)

        arr[0]=0
        
        i=1
        while nums[i-1]==nums[i]:
            arr[nums[0]]+=nums[i]
            i+=1
            
        #arr[nums[0]]=arr[nums[0]]+nums[0]
        
        arr[nums[1]]=arr[nums[1]]+nums[1]
        
        #arr[nums[2]]=arr[nums[2]]+nums[2]

        for i in range(2,len(nums)): 
            
            arr[nums[i]]=max(arr[:(nums[i]-1)])+arr[nums[i]]+nums[i]
            
                #arr[nums[i]]=arr[nums[i]]+nums[i]
        print(arr)
        return(max(arr))
        