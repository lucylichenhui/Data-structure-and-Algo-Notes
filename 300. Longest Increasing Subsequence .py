class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        arr=len(nums)*[0]
        arr[0]=10
        for i in range(1,len(nums)): 
            arr[i]=min(arr[i-1],nums[i])
        print(arr)
        i=0
        cnt=0
        maxc=0
        while i<len(nums): 
            if arr[i]>0: 
                cnt+=1 
            else: 
                cnt=0
            i+=1
            maxc=max(maxc,cnt)
        print(maxc)
                