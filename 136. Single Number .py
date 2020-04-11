class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d= defaultdict(int)
        for k in nums: 
            d[k]+=1
        for k, v in d.items(): 
            if v==1: 
                return k