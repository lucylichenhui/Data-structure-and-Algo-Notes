# Wrong attempt: reason: thought can modify the middle pointer so that we have 3 pointers, 
# But not an option, will result in an infinite while loop. 

class Solution:
    def threeSumClosest():
        nums1=sorted(nums)
        #print(sorted(nums))
        #print(nums)
        i=len(nums1)-1
        a=len(nums1)//2
        j=0
        curr= float("inf")
        while j<i: 
            if a==j: 
                a+=1
                j=0
            if a==i: 
                a+=1
                i=len(nums1)-1
            
            if nums1[i]+nums1[a]+nums1[j]-target>0 : 
                curr=abs(nums1[i]+nums1[a]+nums1[j]-target)
                i-=1
                if i==a: 
                    a-=1
                    i=len(nums)-1
            elif nums1[i]+nums1[a]+nums1[j]-target<0:
                curr=abs(nums1[i]+nums1[a]+nums1[j]-target)
                j+=1
                if j==a: 
                    a+=1
                    j=0
                    
            elif nums1[i]+nums1[a]+nums1[j]-target==0:
                return nums1[i]+nums1[a]+nums1[j]
        return nums1[i]+nums1[a]+nums1[j]





class Solution:
    def threeSumClosest():
        nums.sort()
        sol=float("inf")
        curr= float("inf")
        for midindex in range(len(nums)):
            low, high=midindex+1, len(nums)-1
            while high>low:
                if abs(nums[high]+nums[low]+nums[midindex]-target)<curr:
                    sol=nums[high]+nums[low]+nums[midindex]
                    curr=abs(nums[high]+nums[low]+nums[midindex]-target)
                if nums[high]+nums[low]+nums[midindex]>target: 
                    high-=1
                elif nums[high]+nums[low]+nums[midindex]<target : 
                    low+=1
                elif nums[high]+nums[low]+nums[midindex]==target: 
                    return sol
        return sol

