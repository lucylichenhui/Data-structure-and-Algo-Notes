# Sol1: Brute force sol

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        area=0
        for i in range(len(height)): 
            for j in range(len(height)):
                if j>i: 
                    if min(height[i],height[j])*(j-i)> area: 
                        area=min(height[i],height[j])*(j-i)
        return area


# Sol2: 2 Pointers 
class Solution(object):
    def maxArea(self, height):
        #initialize left and right index first 
        maximum=0
        j=len(height)-1
        i=0 
        while i<j: 
            area=min(height[j],height[i])*(j-i)
            if area>maximum: 
                maximum=area
            if height[j]>height[i]: 
                i+=1 
            else:
                j-=1 
        return maximum
                    
        