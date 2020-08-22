class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if grid == []: #base case solution  
            return 0 
        
        n = len(grid) 
        m = len(grid[0])
        
        visited = [[0] * m for i in range (n)] #m being row, n being column 
        
        def bfs(i,j):
            visited[i][j]=1
            queue = deque([(i,j)]) #always hold indexes in a tuple 
            while queue:
                # print(queue)
                point = queue.pop() 
                i = point[0]
                j = point[1] 
                if i > 0 and visited[i-1][j] == 0 and grid[i-1][j] == "1" : # start from the top left hand corner 
                    queue.append((i-1, j ))
                    visited[i-1][j]=1
                    
                if j > 0 and visited[i][j-1] == 0 and grid[i][j-1] == "1" :
                    queue.append((i, j-1 ))
                    visited[i][j-1]=1
                    
                if i < n-1 and visited[i+1][j] == 0 and grid[i+1][j] == "1" : #start from the bottom right hand corner
                    queue.append((i+1, j ))
                    visited[i+1][j]=1
                    
                if j < m-1 and visited[i][j+1] == 0 and grid[i][j+1] == "1" :
                    queue.append((i, j+1 ))
                    visited[i][j+1]=1
                
            return
        
        count  =0 
        # bfs(0,0)
        # print(visited)
        
        for  i in range (n):
            for j in range(m):
                # print(visited)
                if grid[i][j] == "1" and  visited[i][j]==0 :
                    count +=1
                    bfs(i,j)
        
        return count 
