# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLonelyNodes(self, root: TreeNode) -> List[int]:
        visited = deque([])
        arr=[]
        if root: 
            visited.append(root)
        cur=root
        while cur:

            if cur.left:
                visited.append(cur.left)
                curleft=True
            if cur.right:
                visited.append(cur.right)
                curight=True
            if cur.right and not cur.left: 
                arr.append(cur.right.val)
            elif cur.left and not cur.right: 
                arr.append(cur.left.val)

            visited.popleft()
            if not visited:
                break
            cur = visited[0]
            curleft=False
            curright=False

        return arr