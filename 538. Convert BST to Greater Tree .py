# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.t=0
    
    def convertBST(self, root: TreeNode) -> TreeNode:
        if root is not None: 
            self.convertBST(root.right) 
            self.t+=root.val
            root.val=self.t
            self.convertBST(root.left)
            
        return root
        