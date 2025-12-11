class Solution:
    def deleteDuplicates(self, head):
        prev = sentinel = ListNode(next=head)
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return sentinel.next


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        def helper(head):
            if not head or not head.next:
                return head
            if head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                return helper(head.next)
            else:
                head.next = helper(head.next)
            return head

        return helper(head)
