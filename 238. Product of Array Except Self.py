#my sol: (in On^2)
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        #use queue
        sol=[]
        q=deque(nums)
        #while nums[-1]!=q[0]: 
        for i in nums:
            a=q.popleft()
            s=1
            for e in q: 
                s=s*e
            sol.append(s)
            q.append(a)
        return sol
                
                

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:     
        left, right = [1]*len(nums), [1]*len(nums)
        
        # build left
        for i in range(1, len(nums)):
            left[i] = left[i-1]*nums[i-1]

        # build right
        for i in reversed(range(0, len(nums)-1)):
            right[i] = right[i+1]*nums[i+1]
            
        # build final list
        for i in range(len(nums)):
            nums[i] = left[i]*right[i]
            
        return nums      