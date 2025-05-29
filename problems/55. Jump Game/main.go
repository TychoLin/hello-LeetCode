func canJump(nums []int) bool {
	n := len(nums)
	maxReach := 0
	for i := 0; i < n; i++ {
		if i > maxReach || maxReach >= (n-1) {
			break
		}
		maxReach = max(maxReach, i+nums[i])
	}
	return maxReach >= (n - 1)
}
