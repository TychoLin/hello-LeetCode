class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        sentinel = ListNode(next=head)
        while head:
            while head.next and head.val == head.next.val:
                head.next = head.next.next
            head = head.next
        return sentinel.next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """

        def helper(head):
            if not head or not head.next:
                return head
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
            head.next = helper(head.next)
            return head

        return helper(head)
