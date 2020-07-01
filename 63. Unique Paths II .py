class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        mat = [[1 for x in range(m)] for y in range(n)] 
        for a in range(1,n):
            for b in range(1,m): 
                if obstacleGrid[a-1][b]==1 and obstacleGrid[a][b-1]==1: 
                    mat[a][b]=0
                elif obstacleGrid[a-1][b]==1:
                    mat[a][b]=mat[a][b-1]
                elif obstacleGrid[a][b-1]==1:
                    mat[a-1][b]+mat[a-1][b]
                else:
                    mat[a][b]=mat[a-1][b]+mat[a][b-1]
            
        return mat[n-1][m-1]





class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        #if obstacleGrid==[[1]]: 
            #return 0
        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        mat = [[0 for x in range(m)] for y in range(n)] 
        mat[0][0]=1
        mat[1][0]=1
        mat[0][1]=1
        for a in range(1,n):
            
            for b in range(1,m): 
                if obstacleGrid[a][b]==1: 
                    continue
                
                if obstacleGrid[a-1][b]==1 and obstacleGrid[a][b-1]==1: 
                    mat[a][b]=0
                    
                elif obstacleGrid[a-1][b]==0 and obstacleGrid[a][b-1]==0:
                    mat[a][b]=mat[a-1][b]+mat[a][b-1]
                    
                elif obstacleGrid[a-1][b]==1 and obstacleGrid[a][b-1]==0:
                    mat[a][b]=mat[a][b-1]
                    
                elif obstacleGrid[a][b-1]==1 and obstacleGrid[a-1][b]==0 :
                    mat[a][b]=mat[a-1][b]

            
        print(mat)
        return mat[n-1][m-1]


#final solution




class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        

        n=len(obstacleGrid)
        m=len(obstacleGrid[0])
        
        if n==1 and 1 in obstacleGrid[0]: 
            return 0
        
        if m==1 and [1] in obstacleGrid: 
            return 0
        
        mat = [[0 for x in range(m)] for y in range(n)] 

        if obstacleGrid[0][0]!=1:
            mat[0][0]=1
        else: 
            return 0
            
        if n>1:
            if obstacleGrid[1][0]!=1:
                mat[1][0]=1 
            else: 
                mat[1][0]=0
        if m>1:
            if obstacleGrid[0][1]!=1:
                mat[0][1]=1 
            else: 
                mat[0][1]=0
            
        
        for a in range(0,n):
            for b in range(0,m): 
                
                if a==0 and b==0:  
                    continue 
            
                if  a==1 and b==0:
                    continue

                if a==0 and b==1:
                    continue

                if obstacleGrid[a][b]==1: 
                    mat[a][b]=0
                    continue
                    
                if obstacleGrid[a-1][b]==1 and obstacleGrid[a][b-1]==1: 
                    mat[a][b]=0
                    
                elif obstacleGrid[a-1][b]==0 and obstacleGrid[a][b-1]==0:
                    mat[a][b]=mat[a-1][b]+mat[a][b-1]
                    
                elif obstacleGrid[a-1][b]==1 and obstacleGrid[a][b-1]==0:
                    mat[a][b]=mat[a][b-1]
                    
                elif obstacleGrid[a][b-1]==1 and obstacleGrid[a-1][b]==0 :
                    mat[a][b]=mat[a-1][b]

        print(mat)
        return mat[n-1][m-1]