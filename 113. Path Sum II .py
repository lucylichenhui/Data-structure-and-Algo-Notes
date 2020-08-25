# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def DFS(node,sum1,sum,solution,listheld): 
    
    if not node: return 
    #listheld.append(node.val)
    children=[node.left,node.right]
    if not any(children) and sum1==sum:
        solution.append([sum1,listheld])
    else:
        if node.left:
            DFS(node.left,sum1+node.left.val,sum,solution,listheld+[node.left.val])   
        if node.right:
            DFS(node.right,sum1+node.right.val,sum,solution,listheld+[node.right.val])
        
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root is None: return []
        solution=[]
        listheld=[root.val]
        sum1=root.val
        DFS(root,sum1,sum,solution,listheld)
        print(solution)
        finalsol=[]
        for a,b in solution: 
            if a==sum: 
                finalsol.append(b)
        return finalsol



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        
        if not node:
            return 
        
        # Add the current node to the path's list
        pathNodes.append(node.val)
        
        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)
            
        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()    
    
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList