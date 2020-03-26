# """

# if __name__ == "__main__":
#     # Accept No. of Nodes and edges
#     n, m = map(int, input().split(" "))

#     # Initialising Dictionary of edges
#     g = {}
#     for i in range(n):
#         g[i + 1] = []




#     ----------------------------------------------------------------------------
#         Accepting edges of Unweighted Directed Graphs
#     ----------------------------------------------------------------------------
# """

#     for _ in range(m):
#         x, y = map(int, input().strip().split(" "))
#         g[x].append(y)

#     """
#     ----------------------------------------------------------------------------
#         Accepting edges of Unweighted Undirected Graphs
#     ----------------------------------------------------------------------------
#     """
#     for _ in range(m):
#         x, y = map(int, input().strip().split(" "))
#         g[x].append(y)
#         g[y].append(x)

#     """
#     ----------------------------------------------------------------------------
#         Accepting edges of Weighted Undirected Graphs
#     ----------------------------------------------------------------------------
#     """
#     for _ in range(m):
#         x, y, r = map(int, input().strip().split(" "))
#         g[x].append([y, r])
#         g[y].append([x, r])



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

#=======================================================================================================================#


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