

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sol=0
        for i in range(len(prices)): 
            j=i+1
            while j<len(prices):
                if prices[j]>prices[i]:
                    ans=prices[j]-prices[i]
                    sol=max(sol,ans)
                j+=1
        return sol
                
               