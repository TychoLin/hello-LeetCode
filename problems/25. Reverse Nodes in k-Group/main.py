class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        def helper(head, k):
            runner = head
            count = 0
            while runner and count < k:
                runner = runner.next
                count += 1
            if count < k:
                return head

            prev, cur = None, head
            for _ in range(k):
                new_next = cur.next
                cur.next = prev
                prev = cur
                cur = new_next

            head.next = helper(cur, k)
            return prev

        return helper(head, k)
