# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if root is None : 
            return True
        if root.left and root.left.val!=root.val:
            return False
        if root.right and root.right.val!=root.val: 
            return False
        #if root.left and root.left.val==root.val:
            #return self.isUnivalTree(root.left)
        #if root.right and root.right.val==root.val:
            #return self.isUnivalTree(root.right)
        if self.isUnivalTree(root.right) and self.isUnivalTree(root.left):
            return True
        return False



################################################################################

#Wrong solution

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def rootcount():
    '''
    if root is None: 
        return 0 
    if root.right is not None: 
        return rootcount(root.right, c+1)
    if root.left is not None: 
        return rootcount(root.left, c+1)
    return c
    '''

    if root is None: 
        return 0 
    return 1+rootcount(root.left)+rootcount(root.right)


def recur(): 
    if root.val>=maxi: 
        return False 
    return recur(root.left) and recur(root.left)

        
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        maxi=rootcount()
        return recur()


################################################################################

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def recur(root, index, maxi): 
    if root is None: 
        return True
    if index>=maxi: 
        return False 
    return recur(root.left, 2*index+1, maxi) and recur(root.right,2* index+2, maxi)

def rootcount(root):
    if root is None: 
        return 0 
    return 1+rootcount(root.left)+rootcount(root.right)


class Solution:

    def isCompleteTree(self, root: TreeNode) -> bool:
        global c
        c=0
        index=0
        global maxi
        maxi=rootcount(root)
        if recur(root,index,maxi):
            return True
        else: 
            return False


####################################################################


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def max(root,depth): 
    if root is not None: 
        if root.left: 
            return max(root.left,depth+1)
        if root.right: 
            return max(root.right,depth+1)
    return depth

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if root is None: 
            return 0 
        if not root.left and not root.right: 
            return 1
        depth=1
        return max(root,depth)
        
        

        