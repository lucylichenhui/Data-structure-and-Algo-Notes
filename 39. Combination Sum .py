class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        stack=[]
        def sum1(curr,sumof,target,currlist,stack,temp): 
            if sum(temp)>target:
                return 
            if sum(temp)==target:
                if temp not in stack:
                    stack.append(temp)
                return 
            choices = [sum1(item, sumof, target,currlist[currlist.index(item):],stack,temp+[curr]) for item in currlist]
            return choices
        
        for current in range(0,len(candidates)):
            temp=[]
            sum1(candidates[current],0,target,candidates[current:],stack,temp) 
        return stack