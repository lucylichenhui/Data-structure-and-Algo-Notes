# water trapped is min(prev,next)
# want to find next column with greater or equal height 
# then for every column in the middle, add (column)-that column

class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        i=0
        while i<len(height):
            j=i+1
            while j>i and j<(len(height)):
                if height[j]>=height[i]: 
                    print(i)
                    print(j)
                    break # Found the lower one
                else: 
                    j+=1 
                if j==len(height)-1: 
                    if height[j]>=height[i]: 
                        break
                    i=i+1 
                    j=i+1
            if j-i>1:
                for a in range(i,j):
                    if a!=len(height)-1:
                        added=min(height[i],height[j])-height[a]
                        print(added)
                        water+=added     
            elif j-i==1 and j==len(height)-1: 
                print(i)
                print(j)
                print(height)
                added=height[j]-height[i]
                water+=added
                break
            i=j
                            
        return water 
                



# water trapped is min(prev,next)
# want to find next column with greater or equal height 
# then for every column in the middle, add (column)-that column

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1: 
            return 0
        water=0
        i=0
        j=i+1
        while i<len(height):
            try:
                if height[j]>=height[i] and j<len(height) : 
                    i+=1
                    j+=1
                    
            except: 
                break
            else: 
                print(len(height))
                print(i)
                print(j)
                #try:
                
                while height[i]>height[j] and j<len(height):
                    #while height[i]>height[j] and j<len(height): 
                    j+=1
                    if j==len(height): 
                        j-=1
                        break
                    if i==len(height): 
                        i-=1
                        break
                #except IndexError: 
                    #print("e")
                    #print(i)

                print(j)
                    #if j==len(height)-1: 
                        #break
                for a in range(i+1,j): 
                    water+=max(min(height[i],height[j])-height[a],0)
                    print(water)
            if j==len(height)-1: 
                i+=1
                j=i+1
            #print(i)
            #print(j)
                            
        return water 



# water trapped is min(prev,next)
# want to find next column with greater or equal height 
# then for every column in the middle, add (column)-that column

class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height)==1: 
            return 0
        water=0
        i=0
        j=i+1
        while i<len(height):
            try:
                if height[j]>=height[i] and j<len(height) : 
                    i+=1
                    j+=1
                    
            except: 
                break
            else: 
                
                while height[i]>height[j]:
                    while j<len(height): 
                        j+=1
                #except IndexError: 
                    
                    #break
                    #if j==len(height)-1: 
                        #break
                for a in range(i+1,j): 
                    water+=max(min(height[i],height[j])-height[a],0)
                    print(water)
            if j==len(height)-1: 
                i+=1
                j=i+1
            #print(i)
            #print(j)
                            
        return water


# water trapped is min(prev,next)
# want to find next column with greater or equal height 
# then for every column in the middle, add (column)-that column

class Solution:
    def trap(self, height: List[int]) -> int:
        water=0
        i=0
        while i<len(height):
            j=i+1
            while j>i and j<(len(height)):
                if height[j]>=height[i]: 
                    print(i)
                    print(j)
                    break
                else: 
                    j+=1 
                if j==len(height)-1: 
                    if height[j]>=height[i]: 
                        break
                    i=i+1 
                    j=i+1
            if j-i>1:
                for a in range(i,j):
                    if a!=len(height)-1:
                        added=height[i]-height[a]
                        print(added)
                        water+=added     
            elif j-i==1 and j==len(height)-1: 
                print(i)
                print(j)
                print(height)
                added=height[j]-height[i]
                water+=added
                break
            i=j
                            
        return water 
                

class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        areas = 0
        max_l = max_r = 0
        l = 0
        r = len(height)-1
        while l < r:
            if height[l] < height[r]: # if left is smaller than right 
                if height[l] > max_l: # if left is greater than max of left 
                    max_l = height[l] # assign max of left 
                else:
                    areas += max_l - height[l]
                l +=1
            else:
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    areas += max_r - height[r]
                r -=1
        return areas