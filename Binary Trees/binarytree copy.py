
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
        if root: # basecase, if only root remains 
            visited.append(root) 
            print(root.value)
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

print("Output of Breadth First search is ") 
t.Breadth_first_search(t.root)

######################################################################################################################################################################################################
######################################################################################################################################################################################################


# Python program for expression tree 
  
# An expression tree node 
class Et: 
  
    # Constructor to create a node 
    def __init__(self , value): 
        self.value = value 
        self.left = None
        self.right = None
  
# A utility function to check if 'c' 
# is an operator 
def isOperator(c): 
    if (c == '+' or c == '-' or c == '*'
        or c == '/' or c == '^'): 
        return True
    else: 
        return False
  
# A utility function to do inorder traversal 
def inorder(t): 
    if t is not None: 
        inorder(t.left) 
        print t.value, 
        inorder(t.right) 
  
# Returns root of constructed tree for 
# given postfix expression 
def constructTree(postfix): 
    stack = [] 
  
    # Traverse through every character of input expression 
    for char in postfix : 
  
        # if operand, simply push into stack 
        if not isOperator(char): 
            t = Et(char) 
            stack.append(t) 
  
        # Operator 
        else: 
  
            # Pop two top nodes 
            t = Et(char) 
            t1 = stack.pop() 
            t2 = stack.pop() 
                
            # make them children 
            t.right = t1 
            t.left = t2 
              
            # Add this subexpression to stack 
            stack.append(t) 
  
    # Only element  will be the root of expression tree 
    t = stack.pop() 
     
    return t 

  
# Driver program to test above 
postfix = "ab+ef*g*-"
r = constructTree(postfix) 
print "Infix expression is"
inorder(r) 


######################################################################################################################################################################################################
######################################################################################################################################################################################################


def __int__(self,data): 
    self.data=data
    self.left=None 
    self.right=None 

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
    





