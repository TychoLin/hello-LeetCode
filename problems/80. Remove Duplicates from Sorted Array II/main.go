func removeDuplicates(nums []int) int {
	repeats := 2
	size := len(nums)

	if size <= repeats {
		return size
	}

	k := repeats
	for i := repeats; i < size; i++ {
		if nums[i] != nums[k-repeats] {
			nums[k] = nums[i]
			k++
		}
	}
	return k
}
