func combine(n int, k int) [][]int {
	var result [][]int

	var helper func(start int, path []int)
	helper = func(start int, path []int) {
		left := n - start
		if len(path)+left < k {
			return
		}
		if len(path) == k {
			uniqueCombination := make([]int, k)
			copy(uniqueCombination, path)
			result = append(result, uniqueCombination)
			return
		}

		for i := start; i < n; i++ {
			path = append(path, i+1)
			helper(i+1, path)
			path = path[:len(path)-1]
		}
	}

	helper(0, []int{})
	return result
}
