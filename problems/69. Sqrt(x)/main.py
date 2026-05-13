class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 1
        high = x

        root = 0

        while low <= high:
            mid = (low + high) // 2
            if mid > x // mid:
                high = mid - 1
            else:
                low = mid + 1
            root = high

        return root
