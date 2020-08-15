""" 
Range sum of BST
"""


# empty map instance 
class BSTmap:
    def __init__(self): 
        self.root=None
        self.size=0

    def __len__(self): 
        return self.size
    
    def __iter__(self): 
        return BSTMapIterator(self.root)


class BSTNode:  
    def __init__(): 
        self.key=key
        self.value=value 
        self.left=None 
        self.right=None 



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum=0 
        queue=deque([root])
        if root is "null": 
            return sum
        while queue: 
            current=queue.popleft()
            if current.val<= R and current.val >= L: 
                sum+=current.val
            if current.right and current.val<R: 
                queue.append(current.right)
            if current.left and current.val>L: 
                queue.append(current.left)
        return sum
            
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#my sol
class Solution(object):
    def __init__(self): 
        self.tilt=0
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        #want postorder transversal 
        if not root: 
            return 0
        if not root.right and not root.right: 
            return root.val
        left=self.findTilt(root.left)
        right=self.findTilt(root.right)
        self.tilt+=abs(left-right)
        return self.tilt


#corrections
class Solution:
    def __init__(self):
        self.tilt = 0
        
    def findTilt(self, root):
        self.tilt = 0
        self.helper(root)
        return self.tilt
        
    def helper(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return root.val
        
        leftSum = self.helper(root.left) 
        rightSum = self.helper(root.right)
        
        self.tilt += abs(leftSum-rightSum)
        
        return leftSum + rightSum + root.val

class Solution(object):

    def findTilt(self, root):
        def aux(root):
            if not root: return [0,0]
            left = aux(root.left)
            right = aux(root.right)
            return [left[0]+right[0]+root.val,left[1]+right[1]+abs(left[0]-right[0])]

        return aux(root)[1]