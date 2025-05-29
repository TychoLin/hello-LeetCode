func merge(intervals [][]int) [][]int {
	sort.Slice(intervals, func(i, j int) bool {
		return intervals[i][0] < intervals[j][0]
	})

	merged := [][]int{intervals[0]}

	for _, interval := range intervals[1:] {
		last := merged[len(merged)-1]
		if last[1] < interval[0] {
			merged = append(merged, interval)
		} else {
			if last[1] < interval[1] {
				last[1] = interval[1]
			}
		}
	}

	return merged
}
