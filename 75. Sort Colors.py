class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # No need to use Counting Sort


        index=[0]*3
        
        #cumulate=[0]*3
        
        ans=[0]*len(nums)
        ans=[]
        for i in nums: 
            index[i]+=1
        
        """
        for i in range(len(index)): 
            if i==0: 
                cumulate[i]+=index[i]
            else: 
                cumulate[i]+=sum(index[:i+1])

        """
        
        
        for i in range(index[0]): 
            nums[i]=0
            
        for i in range(index[0],index[1]+index[0]): 
            nums[i]=1
            
        for i in range(index[1]+index[0],index[2]+index[0]+index[1]): 
            nums[i]=2
            
        return nums