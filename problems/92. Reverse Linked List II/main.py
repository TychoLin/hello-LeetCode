class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: Optional[ListNode]
        :type left: int
        :type right: int
        :rtype: Optional[ListNode]
        """
        sentinel = ListNode()
        sentinel.next = head
        prev = sentinel

        for _ in range(left - 1):
            prev = prev.next

        cur = prev.next
        for _ in range(right - left):
            new_insert = cur.next
            cur.next = new_insert.next
            new_insert.next = prev.next
            prev.next = new_insert

        return sentinel.next
