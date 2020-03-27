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
        #length=-1
        
        while queue: 
            
            node, lastcolour,dist=queue.popleft()
            visited.add((lastcolour,node))
            
            if ans[node]==-1: 
                ans[node]=dist 
                
            #newcolour=colour^1
            
            newcolour=lastcolour^1
            for child in graph[node][newcolour] : 
                if (newcolour, child) in visited: 
                    continue 
                        
            #colour=colour^1
                
                queue.append((child, newcolour,dist+1))
        return ans