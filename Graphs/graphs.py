"""

if __name__ == "__main__":
    # Accept No. of Nodes and edges
    n, m = map(int, input().split(" "))

    # Initialising Dictionary of edges
    g = {}
    for i in range(n):
        g[i + 1] = []




    ----------------------------------------------------------------------------
        Accepting edges of Unweighted Directed Graphs
    ----------------------------------------------------------------------------
"""

    for _ in range(m):
        x, y = map(int, input().strip().split(" "))
        g[x].append(y)

    """
    ----------------------------------------------------------------------------
        Accepting edges of Unweighted Undirected Graphs
    ----------------------------------------------------------------------------
    """
    for _ in range(m):
        x, y = map(int, input().strip().split(" "))
        g[x].append(y)
        g[y].append(x)

    """
    ----------------------------------------------------------------------------
        Accepting edges of Weighted Undirected Graphs
    ----------------------------------------------------------------------------
    """
    for _ in range(m):
        x, y, r = map(int, input().strip().split(" "))
        g[x].append([y, r])
        g[y].append([x, r])



"""
--------------------------------------------------------------------------------
    Depth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                S - Traversal Stack
--------------------------------------------------------------------------------
"""


def dfs(G, s):
    vis, S = {s}, [s]
    print(s)
    while S:
        flag = 0
        for i in G[S[-1]]:
            if i not in vis:
                S.append(i)
                vis.add(i)
                flag = 1
                print(i)
                break
        if not flag:
            S.pop()


"""
--------------------------------------------------------------------------------
    Breadth First Search.
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  vis - Set of visited nodes
                Q - Traversal Stack
--------------------------------------------------------------------------------
"""
from collections import deque


def bfs(G, s):
    vis, Q = {s}, deque([s])
    print(s)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if v not in vis:
                vis.add(v)
                Q.append(v)
                print(v)


#=======================================================================================================================#
# Ques and ans implenting BFS annnotated
# Annotated: 25 March
# Source : https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/339965/Python-BFS


from collections import defaultdict, deque

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph = defaultdict(lambda : defaultdict(set))
        #want to be able to insert dict of multiple nested dicts with elements being sets 
        red, blue = 0, 1
        # want to introduce binary var 
        for st, end in red_edges:
            graph[st][red].add(end)
        for st, end in blue_edges:
            graph[st][blue].add(end)
        #for all elements of the graph nodes 
        res = [math.inf] * n
        #math.inf returns a floating point positive infinity
        q = deque([(0,red), (0,blue)])
        # initialize deque as usual, but now require binary var
        level = -1
        while q: #while the transversal stack is not empty
            level += 1 
            size = len(q)
            for i in range(size):
                node, color = q.popleft() #compare node to min node poss 
                opp_color = color^1 #caret operator / XOR 
                res[node] = min(level, res[node])
                neighbors = graph[node][opp_color]
                for child in list(neighbors):
                    graph[node][opp_color].remove(child)
                    q.append((child, opp_color))
        return [r if r != math.inf else -1 for r in res]


def shortestAlternatingPaths(self, n: int, red_edges, blue_edges):
    ans,visited=[-1]*n,{(0,'inf')}
    graph=[[] for _ in range(n)] #used a nested list instead 
    for u,v in red_edges:
        graph[u].append((v,1))
    for u,v in blue_edges:
        graph[u].append((v,-1))
    queue=[(0,'inf',0)] 
    while queue:
        new=[]
        for node,color,dist in queue: # Convention 
            if ans[node]==-1: 
                ans[node]=dist # will take effect from the second iteration onwards, when new node is added
                # also don't have to store this extra var 'dist' in the tuple: no? 多费complexity ha
            for next_node, new_color in graph[node]:
                if new_color!=color and (next_node,new_color) not in visited: # while new colour is not colour and next node and new colour is not in the listed of visited node 
                    new.append((next_node,new_color,dist+1)) 
                    visited.add((next_node,new_color))
        queue=new
    return ans


#Source: https://leetcode.com/problems/shortest-path-with-alternating-colors/discuss/454669/Python-BFS-succinct-solution-with-explanation

from collections import defaultdict, deque
class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: [[int]], blue_edges: [[int]]) -> [int]:
        
        # generate a graph
        graph = defaultdict(set)
        for i, j in red_edges:
            graph[i].add(('r', j))
        for i, j in blue_edges:
            graph[i].add(('b', j))
        
        res = [-1] * n
        
        # BFS
        q = deque([(None, 0, 0)]) # record (color, a_node, shortest dist from node 0 to a_node)
        visited = set() # record (color, vertex) visited
        while q:
            # visit all nodes in q
            last_color, v, dist = q.popleft()
            visited.add((last_color, v))
                
            # specify the distance if hasn't been specified
            if res[v] == -1:
                res[v] = dist
                
            # traverse all child nodes
            for color, child in graph[v]:
                    
                # skip visited edges and edges with the same color as last edge
                if color == last_color or (color, child) in visited:
                    continue
                    
                # add child nodes to a new queue
                q.append((color, child, dist + 1))
            
        return res

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        R=collections.defaultdict(list)
        B=collections.defaultdict(list)
        for u,v in red_edges:
            R[u]+=v,
        for u,v in blue_edges:
            B[u]+=v,
        def mybfs(E):
            ans=[1<<30]*n
            l=0
            vis=set()
            cur=set([0])
            e=0
            while cur:
                nxt=set()
                for u in cur:
                    ans[u]=min(ans[u],l)
                    for v in E[e][u]:
                        if (e,u,v) not in vis:
                            nxt.add(v)
                            vis.add((e,u,v))
                cur=nxt
                e^=1
                l+=1
            return ans
        
        r=mybfs([R,B])
        b=mybfs([B,R])
        o=[min(r[i],b[i]) for i in range(n)]
        return [-1 if p==1<<30 else p for p in o]


class Solution(object):
    def shortestAlternatingPaths(self, n, red_edges, blue_edges):
        """
        :type n: int
        :type red_edges: List[List[int]]
        :type blue_edges: List[List[int]]
        :rtype: List[int]
        """
        queue = [(0,0),(0,1)]
        visited = [[0]*(n) for i in range(2)]
        distance = [-1]*(n)

        graph = collections.defaultdict(list)

        for s,e in red_edges:
                graph[s].append((e,0))
        for s,e in blue_edges:
                graph[s].append((e,1))
        depth = 0
        while queue:
            new_queue = []
            for i in range(len(queue)):
                cn,c = queue.pop(0)
                if visited[c][cn] == 0  :
                    visited[c][cn] = 1
                    if distance[cn] == -1: 
                        distance[cn] = depth 
                for nb,cb in graph[cn]:
                    if cb == (1-c):
                        if visited[cb][nb] == 0:
                            new_queue.append((nb,cb))
            depth += 1
            queue = new_queue
        return distance


############################################
############################################

#My sol

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        graph=[[[],[]] for i in range(n)] 
        red=0
        blue=1
        for u, v in red_edges: 
            graph[u][red].append(v)
        for u, v in blue_edges: 
            graph[u][blue].append(v)
        queue=deque([(0,red,0),(0,blue,0)])
        ans=[-1]*n
        visited=set()
        
        while queue: 
            
            node, lastcolour,dist=queue.popleft()
            visited.add((lastcolour,node))
            
            if ans[node]==-1: 
                ans[node]=dist 
                
            newcolour=lastcolour^1
            for child in graph[node][newcolour] : 
                if (newcolour, child) in visited: 
                    continue 
                
                queue.append((child, newcolour,dist+1))
        return ans
            

                             
#===================================================================================================#

#Island ques BFS solution 


"""

If we see a "1", we know that we have visited an island
want to increment num island by sth we need to do 
want to sink the islands we visit and sink them to 0
Can use either dfs or bfs
Recursive call so need to check indices are valid 

"""

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


#=================================================================================#
#=================================================================================#
#=================================================================================#
#=================================================================================#
#=================================================================================#
#=================================================================================#
#=================================================================================#
#=================================================================================#


#ISLAND PROBLEM 


# Program to count islands in boolean 2D matrix 
class Graph: 
  
    def __init__(self, row, col, g): 
        self.ROW = row 
        self.COL = col 
        self.graph = g 
  
    # A function to check if a given cell  
    # (row, col) can be included in DFS 
    def isSafe(self, i, j, visited): 
        # row number is in range, column number 
        # is in range and value is 1  
        # and not yet visited 
        return (i >= 0 and i < self.ROW and 
                j >= 0 and j < self.COL and 
                not visited[i][j] and self.graph[i][j]) 
              
  
    # A utility function to do DFS for a 2D  
    # boolean matrix. It only considers 
    # the 8 neighbours as adjacent vertices 
    def DFS(self, i, j, visited): 
  
        # These arrays are used to get row and  
        # column numbers of 8 neighbours  
        # of a given cell 
        rowNbr = [-1, -1, -1,  0, 0,  1, 1, 1]; 
            colNbr = [-1,  0,  1, -1, 1, -1, 0, 1]; 
          
        # Mark this cell as visited 
        visited[i][j] = True
  
        # Recur for all connected neighbours 
        for k in range(8): 
            if self.isSafe(i + rowNbr[k], j + colNbr[k], visited): 
                self.DFS(i + rowNbr[k], j + colNbr[k], visited) 


#=================================================================================#
#=================================================================================#

def get_number_of_islands(binaryMatrix):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    # you can use Set if you like
    # or change the content of binaryMatrix as it is visited
    visited = [[0 for col in range(cols)] for r in range(rows)]
    number_of_island = 0
    for row in range(rows):
        for col in range(cols):
            number_of_island += get_island(binaryMatrix, row, col, visited)
    return number_of_island


# get a continuous island
def get_island(binaryMatrix, row, col, visited):
    if not is_valid(binaryMatrix, row, col)
        or visited[row][col] == 1 or binaryMatrix[row][col] == 0:
        return 0

    # mark as visited
    visited[row][col] = 1
    get_island(binaryMatrix, row, col + 1, visited)
    get_island(binaryMatrix, row, col - 1, visited)
    get_island(binaryMatrix, row + 1, col, visited)
    get_island(binaryMatrix, row - 1, col, visited)
    return 1

def is_valid(binaryMatrix, row, col):
    rows = len(binaryMatrix)
    cols = len(binaryMatrix[0])
    return row >= 0 and row < rows and col >= 0 and col < cols


class Solution:
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        global rows 
        global column 
        row=len(grid)
        column=len(grid[0])
        sol=0
        visited=[[0 for i in range(column)] for i in range(row)]

        
        def populate(grid,c,r,visited): 
            
            def is_valid(rows,columns, c, r): 
                return r>=0 and r<row and c>=0 and c<column
    
            
            if not is_valid(row, column, c, r) or visited[r][c]==1 or grid[r][c]==0: 
                    # false case 
                return int(0)
            
            visited[r][c]=1 

            populate(grid, c+1, r, visited)
            populate(grid, c-1, r, visited)
            populate(grid, c, r+1, visited)
            populate(grid, c, r-1, visited)
            return int(1)

        for r in range(row): 
            for c in range(column):
                sol+=populate(grid,c,r,visited)
                
        return sol
    
    
        


#=================================================================================#
#=================================================================================#

    # The main function that returns 
    # count of islands in a given boolean 
    # 2D matrix 
    def countIslands(self): 
        # Make a bool array to mark visited cells. 
        # Initially all cells are unvisited 
        visited = [[False for j in range(self.COL)]for i in range(self.ROW)] 
  
        # Initialize count as 0 and travese  
        # through the all cells of 
        # given matrix 
        count = 0
        for i in range(self.ROW): 
            for j in range(self.COL): 
                # If a cell with value 1 is not visited yet,  
                # then new island found 
                if visited[i][j] == False and self.graph[i][j] == 1: 
                    # Visit all cells in this island  
                    # and increment island count 
                    self.DFS(i, j, visited) 
                    count += 1
  
        return count 
  
  
graph = [[1, 1, 0, 0, 0], 
        [0, 1, 0, 0, 1], 
        [1, 0, 0, 1, 1], 
        [0, 0, 0, 0, 0], 
        [1, 0, 1, 0, 1]] 
  
  
row = len(graph) 
col = len(graph[0]) 
  
g = Graph(row, col, graph) 
  
print "Number of islands is:"
print g.countIslands() 
  
# This code is contributed by Neelam Yadav 
#=======================================================================================================================#



# Python3 program to find the length of the  
# largest region in boolean 2D-matrix  
  
# A function to check if a given cell  
# (row, col) can be included in DFS  
def isSafe(M, row, col, visited): 
    global ROW, COL 
      
    # row number is in range, column number is in  
    # range and value is 1 and not yet visited  
    return ((row >= 0) and (row < ROW) and
            (col >= 0) and (col < COL) and 
            (M[row][col] and not visited[row][col])) 
  
# A utility function to do DFS for a 2D  
# boolean matrix. It only considers  
# the 8 neighbours as adjacent vertices  
def DFS(M, row, col, visited, count): 
      
    # These arrays are used to get row and column  
    # numbers of 8 neighbours of a given cell  
    rowNbr = [-1, -1, -1, 0, 0, 1, 1, 1]  
    colNbr = [-1, 0, 1, -1, 1, -1, 0, 1]  
  
    # Mark this cell as visited  
    visited[row][col] = True
  
    # Recur for all connected neighbours  
    for k in range(8): 
        if (isSafe(M, row + rowNbr[k],  
                   col + colNbr[k], visited)): 
                         
            # increment region length by one  
            count[0] += 1
            DFS(M, row + rowNbr[k],  
                col + colNbr[k], visited, count) 
  
# The main function that returns largest 
# length region of a given boolean 2D matrix  
def largestRegion(M): 
    global ROW, COL 
      
    # Make a bool array to mark visited cells.  
    # Initially all cells are unvisited  
    visited = [[0] * COL for i in range(ROW)] 
  
    # Initialize result as 0 and travesle  
    # through the all cells of given matrix  
    result = -999999999999
    for i in range(ROW): 
        for j in range(COL): 
              
            # If a cell with value 1 is not  
            if (M[i][j] and not visited[i][j]): 
                  
                # visited yet, then new region found  
                count = [1]  
                DFS(M, i, j, visited , count)  
  
                # maximum region  
                result = max(result , count[0]) 
    return result 
  
# Driver Code 
ROW = 4
COL = 5
  
M = [[0, 0, 1, 1, 0], 
     [1, 0, 1, 1, 0],  
     [0, 1, 0, 0, 0], 
     [0, 0, 0, 0, 1]]  
  
print(largestRegion(M)) 
  
# This code is contributed by PranchalK 

#=======================================================================================================================#
#=======================================================================================================================#


#Definition for a undirected graph node
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return 
        nodeCopy = Node(node.val)
        dic = {node: nodeCopy}
        queue = collections.deque([node])
        while queue:
            node = queue.popleft()
            for neighbor in node.neighbors:
                if neighbor not in dic: # neighbor is not visited
                    neighborCopy = Node(neighbor.val)
                    dic[neighbor] = neighborCopy
                    dic[node].neighbors.append(neighborCopy)
                    queue.append(neighbor)
                else:
                    dic[node].neighbors.append(dic[neighbor])
        return nodeCopy
    

#==========================================================================================#

# DFS iteratively
def cloneGraph2(self, node):
    if not node:
        return 
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    stack = [node]
    while stack:
        node = stack.pop()
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = UndirectedGraphNode(neighbor.label)
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                stack.append(neighbor)
            else:
                dic[node].neighbors.append(dic[neighbor])
    return nodeCopy
    
# DFS recursively
def cloneGraph(self, node):
    if not node:
        return 
    nodeCopy = UndirectedGraphNode(node.label)
    dic = {node: nodeCopy}
    self.dfs(node, dic)
    return nodeCopy
    
def dfs(self, node, dic):
    for neighbor in node.neighbors:
        if neighbor not in dic:
            neighborCopy = UndirectedGraphNode(neighbor.label)
            dic[neighbor] = neighborCopy
            dic[node].neighbors.append(neighborCopy)
            self.dfs(neighbor, dic)
        else:
            dic[node].neighbors.append(dic[neighbor])



"""
--------------------------------------------------------------------------------
    Dijkstra's shortest path Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def dijk(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if dist[u] + v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = dist[u] + v[1]
                    path[v[0]] = u
    for i in dist:
        if i != s:
            print(dist[i])


"""
--------------------------------------------------------------------------------
    Topological Sort
--------------------------------------------------------------------------------
"""
from collections import deque


def topo(G, ind=None, Q=None):
    if Q is None:
        Q = [1]
    if ind is None:
        ind = [0] * (len(G) + 1)  # SInce oth Index is ignored
        for u in G:
            for v in G[u]:
                ind[v] += 1
        Q = deque()
        for i in G:
            if ind[i] == 0:
                Q.append(i)
    if len(Q) == 0:
        return
    v = Q.popleft()
    print(v)
    for w in G[v]:
        ind[w] -= 1
        if ind[w] == 0:
            Q.append(w)
    topo(G, ind, Q)


"""
--------------------------------------------------------------------------------
    Reading an Adjacency matrix
--------------------------------------------------------------------------------
"""


def adjm():
    n = input().strip()# n corresponds to the dimension of the adjacency matrix
    #n=int(n)
    a = []
    for i in range(n):
        #dont want nested lists, want list of items 
        a.append(map(int, input().strip().split()))
    print(a)
    return a, n

adjm()

"""
--------------------------------------------------------------------------------
    Floyd Warshall's algorithm
        Args :  G - Dictionary of edges
                s - Starting Node


        Read directly from adjacency matrix 
        Vars :  dist - Dictionary storing shortest distance from s to every other node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""



def floy(A_and_n):
    #let dist be a N*N dimensions matrix 
    (A, n) = A_and_n
    dist = list(A)
    #initialize minimum distances and set toi infinity 
    path = [[0] * n for i in range(n)]
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Pick vertext one by one and include that vertex as an intermediate
                # vertext in the shortest path
                # cost matrix is updated when a shorter path is found 
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
                    path[i][k] = k
    print(dist)

"""
--------------------------------------------------------------------------------
    Prim's MST Algorithm
        Args :  G - Dictionary of edges
                s - Starting Node
        Vars :  dist - Dictionary storing shortest distance from s to nearest node
                known - Set of knows nodes
                path - Preceding node in path
--------------------------------------------------------------------------------
"""


def prim(G, s):
    dist, known, path = {s: 0}, set(), {s: 0}
    while True:
        if len(known) == len(G) - 1:
            break
        mini = 100000
        for i in dist:
            if i not in known and dist[i] < mini:
                mini = dist[i]
                u = i
        known.add(u)
        for v in G[u]:
            if v[0] not in known:
                if v[1] < dist.get(v[0], 100000):
                    dist[v[0]] = v[1]
                    path[v[0]] = u


"""
--------------------------------------------------------------------------------
    Accepting Edge list
        Vars :  n - Number of nodes
                m - Number of edges
        Returns : l - Edge list
                n - Number of Nodes
--------------------------------------------------------------------------------
"""


def edglist():
    n, m = map(int, input().split(" "))
    l = []
    for i in range(m):
        l.append(map(int, input().split(" ")))
    return l, n


"""
--------------------------------------------------------------------------------
    Kruskal's MST Algorithm
        Args :  E - Edge list
                n - Number of Nodes
        Vars :  s - Set of all nodes as unique disjoint sets (initially)
--------------------------------------------------------------------------------
"""


def krusk(E_and_n):
    # Sort edges on the basis of distance
    (E, n) = E_and_n
    E.sort(reverse=True, key=lambda x: x[2])
    s = [{i} for i in range(1, n + 1)]
    while True:
        if len(s) == 1:
            break
        print(s)
        x = E.pop()
        for i in range(len(s)):
            if x[0] in s[i]:
                break
        for j in range(len(s)):
            if x[1] in s[j]:
                if i == j:
                    break
                s[j].update(s[i])
                s.pop(i)
                break


# find the isolated node in the graph
def find_isolated_nodes(graph):
    isolated = []
    for node in graph:
        if not graph[node]:
            isolated.append(node)
    return isolated


