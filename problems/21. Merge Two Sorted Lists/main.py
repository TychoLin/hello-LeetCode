class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        cur = sentinel = ListNode(0)
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                list1 = list1.next
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next
        cur.next = list1 or list2
        return sentinel.next


class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        def helper(list1, list2):
            if not list1:
                return list2
            if not list2:
                return list1
            if list1.val < list2.val:
                list1.next = helper(list1.next, list2)
                return list1
            else:
                list2.next = helper(list1, list2.next)
                return list2
        return helper(list1, list2)
