 
 

def subarraysum(nums,k): 
    c=0
    for i in range(len(nums)-1): 
        j=i+1
        #print(j)
        while j>i and j<len(nums):  
            subarray=nums[i:j]
            #print(subarray)
            if sum(subarray)==k:
                c+=1
            j+=1
    print(c)     
    return c


subarraysum([1,1,1],1)