# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


def maxDepth(node): 
    if node is None: 
        return 0 ;  
  
    else : 
  
        # Compute the depth of each subtree 
        lDepth = maxDepth(node.left) 
        rDepth = maxDepth(node.right) 
  
        # Use the larger one 
        if (lDepth > rDepth): 
            return lDepth+1
        else: 
            return rDepth+1
 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
        stack=[]
        visited=[]
        depth=maxDepth(root)
        #print(depth)
        current=root
        
        while len(stack)<depth: 
            if current is not None: 
# Reach the left most Node of the current Node 

                # Place pointer to a tree node on the stack  
                # before traversing the node's left subtree 
                stack.append(current.val) 
                visited.append(current.val)
                current = current.right  

            elif (stack): 
                current = stack.pop() 
                stack.append(current.val) 
                visited.append(current.val)
                current=current.left

        return visited
    


#corrections


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


 
class Solution:
    def rightSideView(self, root: TreeNode) -> List[int]:
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
            res.append(visitedprev[-1].val)
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

