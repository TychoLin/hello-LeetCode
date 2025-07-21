class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        result = []

        def helper(start, path):
            left = n - start
            if len(path) + left < k:
                return
            if len(path) == k:
                result.append(path[:])
                return

            for i in range(start, n):
                path.append(i + 1)
                helper(i + 1, path)
                path.pop()

        helper(0, [])
        return result
