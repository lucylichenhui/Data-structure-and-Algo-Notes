class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums==[]: 
            return 0
        for i in range(2,len(nums)): 
            nums[i]+=max(nums[:i-1])
        return max(nums[len(nums)-1],nums[len(nums)-2])
    