class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: Optional[ListNode]
        :type k: int
        :rtype: Optional[ListNode]
        """
        if not head or not head.next or k == 0:
            return head

        tail = head
        counter = 1
        while tail.next:
            tail = tail.next
            counter += 1

        k = k % counter
        if k == 0:
            return head

        tail.next = head

        new_tail = head
        for _ in range(counter - k - 1):
            new_tail = new_tail.next

        new_head = new_tail.next
        new_tail.next = None

        return new_head
