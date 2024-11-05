# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        h=[]
        def inorderTraversal(root):
            if root is None:
                return
            inorderTraversal(root.left)
            h.append(root.val)
            inorderTraversal(root.right)
        inorderTraversal(root)
        #h=sorted(h)
        dummy=TreeNode()
        tpt=dummy
        for i in range(len(h)):
            dummy.right=TreeNode(h[i])
            dummy=dummy.right
        return tpt.right