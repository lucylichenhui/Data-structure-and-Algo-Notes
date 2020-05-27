# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool: #DFS
        s=set()
        visited = deque([])
        if root:
            visited.append(root)
        current = root
        s.add(k-current.val)
        while current :
            if current.left:
                if current.left.val in s:
                    return True
                visited.append(current.left)
                s.add(k-current.left.val)
            if current.right:
                if current.right.val in s:
                    return True 
                s.add(k-current.right.val)
                visited.append(current.right)
            visited.popleft()
            if not visited:
                break
            current=visited[0]
        return False
        