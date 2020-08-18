# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        visitedprev= deque([])
        visitedcurr= deque([])
        res=[]
        if root:
            visitedprev.append(root)
            #res.append(root.val)
            #print(root.value)
        current = root
        while visitedprev:
            #print(visitedprev)
            res.append([i.val for i in visitedprev])
            for i in range(len(visitedprev)):
                current=visitedprev.popleft()
                if current.left:
                    #print(current.left.val)
                    visitedcurr.append(current.left)
                if current.right:
                    #print(current.right.val)
                    visitedcurr.append(current.right)
            visitedprev=visitedcurr
            visitedcurr=deque([])
                
        return res

