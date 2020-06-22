class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # 2 neg and 1 pos 
        # 3 pos 
        nums.sort()
        a=nums[len(nums)-1]*nums[len(nums)-2]*nums[len(nums)-3]
        b=nums[0]*nums[1]*nums[len(nums)-1]
        return max(a,b)