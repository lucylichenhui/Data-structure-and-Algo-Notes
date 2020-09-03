class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def partition(string,temp):
            if not string: 
                ans.append(temp)
                return
            for i in string: 
                if temp+[i] not in ans: 
                    partition([item for item in string if item is not i],temp+[i])
        partition(nums,[])
        return ans

