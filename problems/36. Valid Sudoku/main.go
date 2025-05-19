func isValidSudoku(board [][]byte) bool {
	rows := make([]int, 9)
	cols := make([]int, 9)
	boxes := make([]int, 9)

	for i := 0; i < 9; i++ {
		for j := 0; j < 9; j++ {
			if board[i][j] == '.' {
				continue
			}
			val := int(board[i][j] - '0')
			bit := 1 << val
			boxIndex := (i/3)*3 + (j / 3)

			if (rows[i]&bit != 0) || (cols[j]&bit != 0) || (boxes[boxIndex]&bit != 0) {
				return false
			}

			rows[i] |= bit
			cols[j] |= bit
			boxes[boxIndex] |= bit
		}
	}

	return true
}
