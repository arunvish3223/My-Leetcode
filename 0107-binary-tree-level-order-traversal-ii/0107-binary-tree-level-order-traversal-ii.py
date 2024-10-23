# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q=[]
        q.append(root)
        ls=[]
        while(len(q)!=0):
            s=len(q)
            sl=[]
            for i in range(s):
                n=q.pop(0)
                sl.append(n.val)
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ls.append(sl)
        return ls[::-1]
        