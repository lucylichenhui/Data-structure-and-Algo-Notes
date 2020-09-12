
'''
Test case 1
3
aaaba
ababa
aaaca

Test case 2
3 
aabba
aabba
aaacb
'''
#BFS

import math
import operator
from collections import defaultdict
from collections import deque


def bfs(i,j):
    visited[i][j]=1
    queue = deque([(i,j)]) #always hold indexes in a tuple 
    while queue:
        # print(queue)
        point = queue.popleft() 
        i = point[0]
        j = point[1] 
        if i > 0 and visited[i-1][j] == 0 and grid[i-1][j] == grid[i][j] : # start from the top left hand corner 
            queue.append((i-1, j ))
            visited[i-1][j]=1
            
        if j > 0 and visited[i][j-1] == 0 and grid[i][j-1] == grid[i][j] :
            queue.append((i, j-1 ))
            visited[i][j-1]=1
            
        if i < n-1 and visited[i+1][j] == 0 and grid[i+1][j] == grid[i][j]: #start from the bottom right hand corner
            queue.append((i+1, j ))
            visited[i+1][j]=1
            
        if j < m-1 and visited[i][j+1] == 0 and grid[i][j+1] == grid[i][j] :
            queue.append((i, j+1 ))
            visited[i][j+1]=1

    return


h=input()
h=int(h)
grid=[]
for i in range(h): 
    string=raw_input()
    grid.append(string)

n = len(grid) 
m = len(grid[0])

visited = [[0] * m for i in range (n)] #m being row, n being column 

count  =0 


for  i in range (n):
    for j in range(m):
        if grid[i][j]  and  visited[i][j]==0 :
            count +=1
            bfs(i,j)

print(count)

    
