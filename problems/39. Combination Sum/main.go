func combinationSum(candidates []int, target int) [][]int {
	var result [][]int

	var helper func(remaining int, start int, combination []int)
	helper = func(remaining int, start int, combination []int) {
		if remaining == 0 {
			uniqueCombination := append([]int{}, combination...)
			result = append(result, uniqueCombination)
			return
		} else if remaining < 0 {
			return
		}

		for i := start; i < len(candidates); i++ {
			combination = append(combination, candidates[i])
			helper(remaining-candidates[i], i, combination)
			combination = combination[:len(combination)-1]
		}
	}

	helper(target, 0, []int{})
	return result
}
