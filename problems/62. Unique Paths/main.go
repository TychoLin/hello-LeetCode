func uniquePaths(m int, n int) int {
	dp := make([][]int, m+1)
	for i := range dp {
		dp[i] = make([]int, n+1)
	}

	// initial
	dp[0][1] = 1

	// state transition
	for row := 1; row <= m; row++ {
		for col := 1; col <= n; col++ {
			dp[row][col] = dp[row-1][col] + dp[row][col-1]
		}
	}

	return dp[m][n]
}

func uniquePaths(m int, n int) int {
	type Point struct{ x, y int }
	directions := []Point{{0, 1}, {1, 0}}

	dp := make([][]int, m)
	for i := range dp {
		dp[i] = make([]int, n)
	}
	dp[0][0] = 1

	queue := []Point{{0, 0}}

	for len(queue) > 0 {
		p := queue[0]
		queue = queue[1:]

		for _, d := range directions {
			newX, newY := p.x+d.x, p.y+d.y

			if newX >= 0 && newX < m && newY >= 0 && newY < n {
				if dp[newX][newY] == 0 {
					queue = append(queue, Point{newX, newY})
				}
				dp[newX][newY] += dp[p.x][p.y]
			}
		}
	}

	return dp[m-1][n-1]
}

func uniquePaths(m int, n int) int {
	dp := make([]int, n+1)

	// initial
	dp[1] = 1

	// state transition
	for row := 1; row <= m; row++ {
		for col := 1; col <= n; col++ {
			dp[col] += dp[col-1]
		}
	}

	return dp[n]
}
