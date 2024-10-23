# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        q=[]
        q.append(root)
        ls=[]
        while(len(q)!=0):
            s=len(q)
            sum=0
            for i in range(s):
                n=q.pop(0)
                sum+=n.val
                if n.left:
                    q.append(n.left)
                if n.right:
                    q.append(n.right)
            ls.append(sum)
        root.val=0
        q.append(root)
        level=1
        while(len(q)!=0):
            s=len(q)
            for i in range(s):
                n=q.pop(0)
                sum=0
                if n.left:
                    sum+=n.left.val
                if n.right:
                    sum+=n.right.val
                if n.left:
                    n.left.val=ls[level]-sum
                    q.append(n.left)
                if n.right:
                    n.right.val=ls[level]-sum
                    q.append(n.right)
            level+=1
        return root
        

        