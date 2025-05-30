class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        cur = head

        while cur:
            new_cur = cur.next
            cur.next = prev
            prev = cur
            cur = new_cur

        return prev
