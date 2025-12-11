class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """
        cur = sentinel = ListNode(next=head)
        while cur.next:
            if cur.next.val == val:
                cur.next = cur.next.next
            else:
                cur = cur.next
        return sentinel.next


class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: Optional[ListNode]
        :type val: int
        :rtype: Optional[ListNode]
        """

        def helper(head, val):
            if not head:
                return None
            head.next = helper(head.next, val)
            return head.next if head.val == val else head

        return helper(head, val)
