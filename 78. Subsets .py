class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def partition(temp): 
            if not temp: 
                return
            ans.append(temp)
            for i in temp:
                if [item for item in temp if item is not i] not in ans:
                    partition([item for item in temp if item is not i])
        partition(nums)
        ans.append([])
        return ans