class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)==0: 
            return False
        arr=[1]*len(nums)
        maxcnt=1
        for i in range(1,len(nums)): 
            cnt=0
            for j in range(i): 
                if nums[i]>nums[j]: 
                    cnt=max(arr[j]+1,1)
                    arr[i]=max(cnt,arr[i])
                    maxcnt=max(arr[i],maxcnt)    
                    if maxcnt==3: 
                        return True 
        return False                