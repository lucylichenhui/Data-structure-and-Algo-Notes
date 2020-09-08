class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int: 
        from heapq import heappush, heappop, heapreplace, heapify
        s=[-1*i for i in stones]
        heapify(s)
        while len(s)>=2:
            a=heappop(s)
            b=heappop(s)
            if a!=b: 
                heappush(s,min([a,b])-max([a,b]))
        if not s: 
            return 0
        else: 
            for a in s:
                return -a


            