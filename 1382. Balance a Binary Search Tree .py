# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

#def treetoarray(root,): 
    #if current.left: 


#IMPORTANT: YOU NEED IN ORDER TRAVERSAL       
#traverse left tree first, then root, then right tree 

def inordertrav(subtree): 
    if subtree is not None: 
        inordertrav(subtree.left)
        l.append(subtree.val)
        inordertrav(subtree.right)

def sortedArrayToBST(arr): 
    if not arr: 
        return None
    mid = (len(arr)) // 2
    root = TreeNode(arr[mid]) 
    root.left = sortedArrayToBST(arr[:mid]) 
    root.right = sortedArrayToBST(arr[mid+1:]) 
    return root 

class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        global l
        l=[]
        inordertrav(root)
        
        return sortedArrayToBST(l)