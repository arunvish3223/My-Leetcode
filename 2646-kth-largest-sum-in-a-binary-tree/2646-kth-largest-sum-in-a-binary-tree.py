# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        min_heap = []
        queue = deque([root])
        while queue:
            level_sum = 0
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                level_sum += curr.val

                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)

            heapq.heappush(min_heap, level_sum)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return -1 if len(min_heap) < k else min_heap[0]
        