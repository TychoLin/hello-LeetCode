class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """
        lt_sentinel = ListNode()
        gte_sentinel = ListNode()

        lt_cur = lt_sentinel
        gte_cur = gte_sentinel

        while head:
            if head.val < x:
                lt_cur.next = head
                lt_cur = lt_cur.next
            else:
                gte_cur.next = head
                gte_cur = gte_cur.next
            head = head.next

        gte_cur.next = None
        lt_cur.next = gte_sentinel.next

        return lt_sentinel.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        def helper(node, lt_cur, gte_cur):
            if not node:
                return lt_cur, gte_cur
            if node.val < x:
                lt_cur.next = node
                lt_cur = node
            else:
                gte_cur.next = node
                gte_cur = node
            return helper(node.next, lt_cur, gte_cur)

        lt_sentinel = ListNode()
        gte_sentinel = ListNode()
        lt_cur, gte_cur = helper(head, lt_sentinel, gte_sentinel)
        gte_cur.next = None
        lt_cur.next = gte_sentinel.next
        return lt_sentinel.next


class Solution(object):
    def partition(self, head, x):
        """
        :type head: Optional[ListNode]
        :type x: int
        :rtype: Optional[ListNode]
        """

        def helper(node):
            if not node:
                return None, None, None, None
            lt_head, lt_tail, gte_head, gte_tail = helper(node.next)
            node.next = None
            if node.val < x:
                if not lt_head:
                    lt_head = lt_tail = node
                else:
                    node.next = lt_head
                    lt_head = node
            else:
                if not gte_head:
                    gte_head = gte_tail = node
                else:
                    node.next = gte_head
                    gte_head = node
            return lt_head, lt_tail, gte_head, gte_tail

        lt_head, lt_tail, gte_head, gte_tail = helper(head)
        if lt_tail:
            lt_tail.next = gte_head
            return lt_head
        else:
            return gte_head
