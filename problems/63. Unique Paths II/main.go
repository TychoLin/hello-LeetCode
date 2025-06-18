func uniquePathsWithObstacles(obstacleGrid [][]int) int {
	m := len(obstacleGrid)
	n := len(obstacleGrid[0])

	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	// initial
	dp[0][1] = 1

	// state transition
	for row := 1; row <= m; row++ {
		for col := 1; col <= n; col++ {
			if obstacleGrid[row-1][col-1] == 1 {
				dp[row][col] = 0
			} else {
				dp[row][col] = dp[row-1][col] + dp[row][col-1]
			}
		}
	}

	return dp[m][n]
}
