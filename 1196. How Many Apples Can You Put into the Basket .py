class Solution:
    def maxNumberOfApples(self, arr: List[int]) -> int:
        arr.sort()
        sum=0
        num=0
        print(arr)
        for i in arr: 
            sum+=i
            num+=1
            if sum>5000: 
                num-=1
                break
        return num