class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        if len(nums)==1: 
            return nums[0]
        negative=(len(nums))*[0]
        positive=(len(nums))*[0]

        if nums[0]>=0: 
            positive[0]=nums[0]
        else: 
            negative[0]=nums[0]
        
        maxsum=-float("inf")
        
        for i in range(1,len(nums)): 
            if max(nums[i],nums[i]*negative[i-1],nums[i]*positive[i-1])>0: 
                positive[i]=max(nums[i],nums[i]*negative[i-1],nums[i]*positive[i-1])
            if min(nums[i],nums[i]*negative[i-1],nums[i]*positive[i-1])<0:
                negative[i]=min(nums[i],nums[i]*negative[i-1],nums[i]*positive[i-1])
            maxsum=max(positive[i],maxsum)

        return max(maxsum,nums[0])