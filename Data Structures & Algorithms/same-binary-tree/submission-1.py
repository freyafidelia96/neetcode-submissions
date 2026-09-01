# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True

        q1 = deque([p])
        q2 = deque([q])

        while q1 and q2:
            n1 = q1.popleft()
            n2 = q2.popleft()

            if n1 is None and n2 is None:
                continue

            if not n1 or not n2 or n1.val != n2.val:
                return False
    
            if n1:
                q1.append(n1.left)
                q1.append(n1.right)
            if n2:
                q2.append(n2.left)
                q2.append(n2.right)

        if len(q1) != len(q2):
            return False
        return True
        
        