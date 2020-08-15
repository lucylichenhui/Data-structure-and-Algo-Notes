
""" 

Binary Tree 

"""


class Node(object):
    def __init__(self, value,left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class BinarySearchTree(object):
    def __init__(self, value):
        self.root = Node(value)


    def insert(self, value):
        current = self.root
        while current: # while self root
            if value > current.value: #if value is greater than curr.value, assign Node(value) to current.right
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right #then iteratively assign curr.right to curr 
            else: # repeat the same process for left 
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left


    def Breadth_first_search(self,root):
        """In BFS the Node Values at each level of the Tree are traversed before going to next level"""

        visited = deque([])
        if root:
            visited.append(root)
            print root.value
        current = root
        while current :
            if current.left:
                print(current.left.value)
                visited.append(current.left)
            if current.right:
                print(current.right.value)
                visited.append(current.right)
            visited.popleft()
            if not visited:
                break
            current = visited[0]


t = BinarySearchTree(100)
t.insert(12)
t.insert(92)
t.insert(112)
t.insert(123)
t.insert(2)
t.insert(11)
t.insert(52)
t.insert(3)
t.insert(66)
t.insert(10)

print "Output of Breadth First search is "
t.Breadth_first_search(t.root)

def __inti__(self,data): 
    self.data=data
    self.left=None 
    self.right=None 

#preorder traversal
def traverse(subtree): 
    if subtree is not None:  #note, not self 
        print(subtree.data)
        traverse(subtree.right)
        traberse(subtree.left)


#traverse left tree first, then root, then right tree 
def inordertrav(subtree): 
    if subtree is not None: 
        inorderTrav(subtree.left)
        print(subtree.data)
        inorderTrav(subtree.right)

#traverse lefttree first, then right tree, then root
def posordertrav(subtree): 
    if subtree is not None: 
        inorderTrav(subtree.left)
        inorderTrav(subtree.right)
        print(subtree.data)


def BFStransversal(subtree): 
    pass 
    


#================================================================================#
"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.
""" 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


def traverse(subtree): 
    ans=[]
    if subtree is not None:  #note, not self 
        ans.append(subtree.val)
        if subtree.right is None: 
            ans.append("null")
        traverse(subtree.right)
        if subtree.left is None: 
            ans.append("null")
        traverse(subtree.left)
    return ans 

class Solution(object):
    def isSameTree(self, p, q):
        outputfield=traverse(p)
        outputfield1=traverse(q)
        if outputfield1==outputfield: 
            return "true"
        else: 
            return "false"
        

        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

#================================================================================#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSameTree(self, p, q):
        if p and q: 
            return p.val==q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        if not p and not q: 
            return True 
        else: 
            return False


