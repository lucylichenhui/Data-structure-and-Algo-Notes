# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':

        stack=[] # just in case we need option 2 
        
        old=None
        new=None

        # implement option 1
        curr=p
        current=root
        
        if not curr: 
            return None
        
        if curr.right:
            curr=curr.right
            while curr.left: 
                curr=curr.left 
            return curr


        # implement option 2 
        
        else:
            while True: 
                # Reach the left most Node of the current Node 
                if current is not None: 

                    # Place pointer to a tree node on the stack  
                    # before traversing the node's left subtree 
                    stack.append(current) 

                    current = current.left  

                # BackTrack from the empty subtree and visit the Node 
                # at the top of the stack; however, if the stack is  
                # empty you are done 
                elif(stack): 
                    current = stack.pop() 
                    old=new
                    if old==p: 
                        return current
                    new=current # Python 3 printing 
                    # We have visited the node and its left  
                    # subtree. Now, it's right subtree's turn 
                    current = current.right  

                else: 
                    break

            #return f

