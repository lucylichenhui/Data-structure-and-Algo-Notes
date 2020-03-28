

## Insertion sort##

for loop_index in range(1, len(collection)):
    insertion_index = loop_index
    while (
        insertion_index > 0
        and collection[insertion_index - 1] > collection[insertion_index]
    ):
        collection[insertion_index], collection[insertion_index - 1] = (
            collection[insertion_index - 1],
            collection[insertion_index],
        )
        insertion_index -= 1

return collection


    """
        for i in range(1, len(nums)): 
            j=i-1
            nextelement=nums[i]
            while (nums[i])>nextelement and j>0: 
                nums[j]=nums[j+1]
                j=j-1
                nums[j+1]=nextelement
        return nums
    """


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        for loop_index in range(1, len(nums)):
            insertion_index = loop_index
            while insertion_index > 0 and nums[insertion_index - 1] > nums[insertion_index]:
                nums[insertion_index]=nums[insertion_index - 1]
                nums[insertion_index - 1] = nums[insertion_index]
                insertion_index -= 1

        return nums
    

#variation 
class Solution:
    def insertionSort(self, nums): 
    # Traverse through 1 to len(nums) 
        for i in range(1, len(nums)): 

            key = nums[i] 

            # Move elements of arr[0..i-1], that are 
            # greater than key, to one position ahead 
            # of their current position 
            j = i-1
            while j >= 0 and key < nums[j] : 
                    nums[j + 1] = nums[j] 
                    j -= 1
            nums[j + 1] = key 
        return nums
        
    def sortArray(self, nums: List[int]) -> List[int]:
        self.insertionSort(nums)
        return nums




## BB sort##


def bbsort(self, nums): 
    for iteritem in range(len(nums)-1, 0, -1): 
        for idx in range(iteritem):
            if nums[idx]>nums[idx+1]:
                temp= nums[idx]
                nums[idx]=nums[idx+1]
                nums[idx+1]=temp
    return nums

## Q sort


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        self.quicksort(nums, 0, len(nums) - 1)
        return nums
    
    def quicksort(self, nums, lower, upper):
        if lower < upper:
            pivot = self.partition(nums, lower, upper)
            self.quicksort(nums, lower, pivot - 1)
            self.quicksort(nums, pivot + 1, upper)
        else:
            return
        
    def partition(self, nums, lower, upper):
        
        pivot = nums[upper]
        
        i = lower
        
        for j in range(lower, upper):
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                
        nums[i], nums[upper] = nums[upper], nums[i]
        
        return i