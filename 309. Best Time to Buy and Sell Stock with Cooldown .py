class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        array=[0]*len(prices)
        i=0
        while i+1<len(prices): 
            while prices[i]<prices[i+1] : 
                if i==0: 
                    array[i]="L"
                else:
                    array[i]=0
                i+=1
                if i+1>=len(prices): 
                    break
            if i+1>=len(prices): 
                    break
            while prices[i]>prices[i+1] : 
                if array[i-1]!="H":
                    array[i]="H"
                i+=1
                if i+1>=len(prices): 
                    break
                
                
        print(array)
                



