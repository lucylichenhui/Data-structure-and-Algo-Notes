class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def partition(string,temp):
            if len(temp)==k: 
                ans.append(sorted(temp))
                return
            for i in string: 
                if sorted(temp+[i]) not in ans: 
                    partition([item for item in string if item is not i],temp+[i])
        partition([i for i in range(1,n+1)],[])
        return ans

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans=[]
        def partition(index=1,temp=[]):
            if len(temp)==k: 
                ans.append(temp[:])
                #return
            for i in range(index,n+1): 
                temp.append(i)
                partition(i+1,temp)
                temp.pop()
        partition()
        return ans



