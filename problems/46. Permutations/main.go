func permute(nums []int) [][]int {
	var result [][]int
	var path []int
	used := make([]bool, len(nums))

	var helper func()
	helper = func() {
		if len(path) == len(nums) {
			permutation := append([]int{}, path...)
			result = append(result, permutation)
			return
		}
		for i := 0; i < len(nums); i++ {
			if !used[i] {
				used[i] = true
				path = append(path, nums[i])
				helper()
				path = path[:len(path)-1]
				used[i] = false
			}
		}
	}

	helper()
	return result
}
