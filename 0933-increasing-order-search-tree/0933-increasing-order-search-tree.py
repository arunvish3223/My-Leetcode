# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        stk=[]
        dummy=TreeNode(0)
        tpt=dummy
        while stk or root:
            while root:
                stk.append(root)
                root =root.left
            root =stk.pop()
            tpt.right=root
            tpt=tpt.right
            root = root.right
            tpt.left=None
        return dummy.right

