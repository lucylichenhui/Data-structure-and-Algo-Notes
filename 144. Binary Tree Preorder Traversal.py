# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        current = root  
        stack = [] # initialize stack 
        f=[]
        done = 0 

        # append the root node to the stack 
        if current is not None: 
            stack.append(current)
            #f.append(current.val)
        
        while stack: 
            curr=stack.pop()
            f.append(curr.val)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        
        return f