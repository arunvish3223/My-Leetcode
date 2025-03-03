class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val < x:
                before.next, before = head, head
            else:
                after.next, after = head, head
            head = head.next

        after.next = None
        before.next = after_head.next
        return before_head.next