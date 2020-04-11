


nums= [6,5,4,8]
solution=[]
for i in range(len(nums)): 
    j=0
    sol=0
    while j<len(nums): 
        if j!=i:
            if nums[j]<nums[i]: 
                sol+=1
        j+=1
    solution.append(sol)
        
print(solution)
            