class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0 for col in range(n + 1)] for row in range(m + 1)]

        # initial
        dp[0][1] = 1

        # state transition
        for row in range(1, m + 1):
            for col in range(1, n + 1):
                if obstacleGrid[row - 1][col - 1] == 1:
                    dp[row][col] = 0
                else:
                    dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m][n]
