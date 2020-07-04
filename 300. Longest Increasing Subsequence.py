class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums)==0: 
            return 0
        arr=[1]*len(nums)
        maxcnt=1
    
        for i in range(1,len(nums)): 
            cnt=0
            for j in range(i): 
                if nums[i]>nums[j]: 
                    cnt=max(arr[j]+1,1)
                    arr[i]=max(cnt,arr[i])
                    maxcnt=max(arr[i],maxcnt)    
                
        return maxcnt
                
            