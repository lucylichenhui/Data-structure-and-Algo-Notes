# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        global lprev
        #lnew=None
        global l
        l=[]

        def inordertrav(subtree): 
            global l
            if subtree is not None: 
                inordertrav(subtree.left)
                l.append(subtree.val)
                inordertrav(subtree.right)
            return l

        list=inordertrav(root)
        #print(sorted(l))
        #print([i for i in range(1,len(list))])
        
        if len(list)==1: 
            return True
        
        if list==[i for i in range(1,len(list)+1)]:
            return True
        else: 
            return False


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        global lprev
        lprev=float("inf")
        #lnew=None

        def inordertrav(subtree): 
            global lprev
            if subtree is not None: 
                inordertrav(subtree.left)
                if subtree.val>=lprev: 
                    return False, lprev
                lprev=subtree.val
                inordertrav(subtree.right)
            return True, lprev

        #print(lprev)
        if inordertrav(root):
            return True
        else: 
            return False




# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right





class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        current = root  
        stack = [] # initialize stack 
        f=-float("inf")
        done = 0 

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
                if current.val<=f: 
                    return False
                else:
                    f=current.val
                # We have visited the node and its left  
                # subtree. Now, it's right subtree's turn 
                current = current.right  

            else: 
                break
                
        return True

