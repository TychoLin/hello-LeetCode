func removeDuplicates(nums []int) int {
	k := 1
	for cur := 1; cur < len(nums); cur++ {
		if nums[cur] != nums[cur-1] {
			nums[k] = nums[cur]
			k += 1
		}
	}
	return k
}
