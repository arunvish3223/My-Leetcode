# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binary_tree_pruning(self, root):
        if root is None:
            return None
        root.left = self.binary_tree_pruning(root.left)
        root.right = self.binary_tree_pruning(root.right)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.binary_tree_pruning(root)
