

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        n=len(grid)
        m=len(grid[0])
        
        for a in range(0,n):
            for b in range(0,m):                  
                if a==0 and b==0:  
                    continue 
                elif b==0:
                    grid[a][b]+=grid[a-1][b]
                elif a==0:
                    grid[a][b]+=grid[a][b-1]
                else: 
                    grid[a][b]+=min(grid[a-1][b],grid[a][b-1])

        #print(grid)
        return grid[n-1][m-1]
            