class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bfs
        mat = [[0 for x in range(m)] for y in range(n)] 
        visited=deque([[0,0,1]])#queue
        mat[0][0]=1
        i=0
        j=0
        
        while visited: #i row, j column 
            i,j,cnt=visited.popleft()   
            if i+1<n and j<m:
                mat[i+1][j]+=1
                visited.append([i+1,j,mat[i+1][j]])

            if i<n and j+1<m:
                mat[i][j+1]+=1
                visited.append([i,j+1,mat[i][j+1]])
            
        return cnt
            


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #bfs
        mat = [[1 for x in range(m)] for y in range(n)] 
        #mat[0][0]=1
        for a in range(1,n):
            for b in range(1,m): 
                mat[a][b]=mat[a-1][b]+mat[a][b-1]
            
        return mat[n-1][m-1]
            
        
        