class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def helper(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry
            node = ListNode(total % 10)
            node.next = helper(n1.next if n1 else None,
                               n2.next if n2 else None, total // 10)
            return node

        return helper(l1, l2, 0)


class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def helper(n1, n2, carry):
            if not n1 and not n2 and carry == 0:
                return None

            val1 = n1.val if n1 else 0
            val2 = n2.val if n2 else 0
            total = val1 + val2 + carry
            node = ListNode(total % 10)
            node.next = helper(n1.next if n1 else None,
                               n2.next if n2 else None, total // 10)
            return node

        return helper(l1, l2, 0)
