class Solution:
    
    
    def numIslands(self, grid: List[List[str]]) -> int:

        row=len(grid)
        column=len(grid[0])
        sol=0
        visited=[[0 for i in range(column)] for i in range(row)]

        
        def is_valid(rows,columns, c, r): 
            return r>=0 and r<row and c>=0 and c<column
    
            
        def populate(grid,c,r,visited): 
            
            if not is_valid(row, column, c, r) or visited[r][c]==1 or grid[r][c]==0: 
                return 0
                 
                    # false case 
                visited[r][c]=1 

                populate(grid, c+1, r, visited)
                populate(grid, c-1, r, visited)
                populate(grid, c, r+1, visited)
                populate(grid, c, r-1, visited)

            return 1

        for r in range(row): 
            for c in range(column):
                sol+=populate(grid,c,r,visited)
                
        return sol
    
    
        

def get_number_of_islands(grid):
    rows = len(grid)
    cols = len(grid[0])
    # you can use Set if you like
    # or change the content of binaryMatrix as it is visited
    visited = [[0 for col in range(cols)] for r in range(rows)]
    number_of_island = 0
    for row in range(rows):
        for col in range(cols):
            number_of_island += get_island(grid, row, col, visited)
    return number_of_island


# get a continuous island
def get_island(grid, row, col, visited):
    if not is_valid(grid, row, col)
        or visited[row][col] == 1 or grid[row][col] == 0:
        return 0

    # mark as visited
    visited[row][col] = 1
    get_island(grid, row, col + 1, visited)
    get_island(grid, row, col - 1, visited)
    get_island(grid, row + 1, col, visited)
    get_island(grid, row - 1, col, visited)
    return 1


def is_valid(grid, row, col):
    rows = len(grid)
    cols = len(grid[0])
    return row >= 0 and row < rows and col >= 0 and col < cols