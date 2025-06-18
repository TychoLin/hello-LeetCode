class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        dp = [[0 for col in range(n + 1)] for row in range(m + 1)]

        # initial
        dp[0][1] = 1

        # state transition
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m][n]
