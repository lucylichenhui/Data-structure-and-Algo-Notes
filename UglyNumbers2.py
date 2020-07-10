class Solution:
    def nthUglyNumber(self, n: int) -> int:
        d=[float(0)]*(n+1)
        if n==0: 
            return 0
        if n==1: 
            return 1
        
        if n==2: 
            return 2
        if n==3: 
            return 3
        if n==4: 
            return 4
        
        if n==5: 
            return 5
        

        
        d[0]=0
        d[1]=1
        d[2]=2
        d[3]=3
        d[4]=4
        d[5]=5
            
        l=[2,3,5]
        
        for i in range(6,n+1): 
            minin=float("inf")
            #u=minin
            for j in range(i): 
                for a in l:
                    if d[j]*d[a]>d[i-1]:
                        minin=min(minin,d[j]*d[a])
                        #u=min(u,minin)
                        d[i]=minin
        return(d[n])


class Ugly:
    def __init__(self):
        self.nums = nums = [1, ]
        i2 = i3 = i5 = 0

        for i in range(1, 1690):
            ugly = min(nums[i2] * 2, nums[i3] * 3, nums[i5] * 5)
            nums.append(ugly)

            if ugly == nums[i2] * 2: 
                i2 += 1
            if ugly == nums[i3] * 3:
                i3 += 1
            if ugly == nums[i5] * 5:
                i5 += 1
            
class Solution:
    u = Ugly()
    def nthUglyNumber(self, n):
        return self.u.nums[n - 1]
                
