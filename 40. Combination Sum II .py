
# Edit lol you noob
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack=[]
        def sum1(curr,sumof,target,current,currlist,stack,temp): 
            if sum(temp)>target:
                return 
            if sum(temp)==target:
                if sorted(temp) not in stack:
                    stack.append(sorted(temp))
                return 
            choices = [sum1(currlist, sumof, target,current,currlist[current+1:],stack,temp+[curr]) for current in range(currlist)]
            return choices
        for current in range(len(candidates)):
            temp=[]
            sum1(candidates[current],0,target,current,candidates[current+1:],stack,temp) 
        return stack



# Edit lol you noob
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        stack=[]
        def sum1(curr,sumof,target,current,currlist,stack,temp): 
            if sum(temp)>target:
                return 
            if sum(temp)==target:
                if sorted(temp) not in stack:
                    stack.append(sorted(temp))
                return 
            choices = [sum1(currlist, sumof, target,current,currlist[current+1:],stack,temp+[curr]) for current in range(currlist)]
            return choices
        for current in range(len(candidates)):
            temp=[]
            sum1(candidates[current],0,target,current,candidates[current+1:],stack,temp) 
        return stack



class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(remain, combo, index):
            if remain == 0:
                if combo not in result:
                    result.append(combo)
                return
            for i in range(index, len(candy)):
                if candy[i] > remain:
                    break 
                dfs(remain - candy[i], combo + [candy[i]], i+1)
                
        candy = sorted(candidates)
        result = []
        dfs(target, [], 0)
        return result