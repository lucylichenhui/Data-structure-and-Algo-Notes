#1214. Two Sum BSTs

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def twoSumBSTs(self, root1: TreeNode, root2: TreeNode, target: int) -> bool:
        s=set()
        visited = deque([])
        if root1:
            visited.append(root1)
        current = root1
        s.add(target-current.val)
        while current:
            if current.left:
                visited.append(current.left)
                s.add(target-current.left.val)
            if current.right:
                s.add(target-current.right.val)
                visited.append(current.right)
            visited.popleft()
            if not visited:
                break
            current=visited[0]
            
        #print(s)
        if root2:
            visited.append(root2)
        
        current = root2
        if current.val in s: 
            return True
        visited = deque([current])
        #s.add(target-current.val)
        while current:
            if current.left:
                if current.left.val in s:
                    return True 
                visited.append(current.left)

            if current.right:
                if current.right.val in s: 
                    return True 
                visited.append(current.right)

            visited.popleft()
            if not visited:
                break
            current=visited[0]
        return False  