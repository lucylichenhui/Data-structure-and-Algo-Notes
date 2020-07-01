class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        d=[float("inf")]*(amount+1)
        d[0]=0
        for c in coins: 
            for i in range(c, amount+1): 
                d[i]=min(d[i],d[i-c]+1)
        return d[amount] if d[amount]!= float("inf") else -1
        
        