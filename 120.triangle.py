class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        
        for row in range(1,len(triangle)): 
            for index in range(len(triangle[row])): 
                if index!=0 and index!=len(triangle[row])-1:
                    triangle[row][index]=min(triangle[row-1][index],triangle[row-1][index-1])+triangle[row][index]
                elif index==0: 
                    triangle[row][index]=triangle[row-1][index]+triangle[row][index]
                elif index==len(triangle[row])-1: 
                    triangle[row][index]=triangle[row-1][index-1]+triangle[row][index]
                    
        
        return min(triangle[len(triangle)-1])