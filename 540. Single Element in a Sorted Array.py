class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        if len(nums)==0: 
            return 
        if len(nums)==1: 
            for i in nums: 
                return i
        i=0
        while i+1<len(nums): 
            first=nums[i]
            second=nums[i+1]
            if first==second: 
                i=i+2
            else:
                return first
        return nums[-1]


