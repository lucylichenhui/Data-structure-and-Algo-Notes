# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def DFS(node,sum1,sum,solution,i): 
    
    children=[node.left,node.right]
    if not any(children):
        solution.append(sum1)
        
    if not node: return 

    if node.left:            
        DFS(node.left,sum1+node.left.val,sum,solution,i+1)   

    if node.right:
        DFS(node.right,sum1+node.right.val,sum,solution,i+1)
        
# use recursion 
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None: return 0
        solution=[]
        sum1=root.val
    
        
        x=DFS(root,sum1,sum,solution,0)
        #print(x)
        print(solution)
        for i in solution: 
            if i==sum: 
                return True
            
        return False
        
            