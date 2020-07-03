class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if prices==[]: 
            return 0
        if len(prices)==1: 
            return 0
        f=[-float("inf")]*(len(prices))
        for i in range(1,len(prices)): 
            f[i]=prices[i]-min(prices[:i])
        return max(max(f),0)