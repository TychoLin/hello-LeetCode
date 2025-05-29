func canReach(arr []int, start int) bool {
	visited := make([]bool, len(arr))

	var helper func(start int) bool
	helper = func(start int) bool {
		if start >= len(arr) || start < 0 || visited[start] {
			return false
		}
		if arr[start] == 0 {
			return true
		}

		visited[start] = true

		return helper(start+arr[start]) || helper(start-arr[start])
	}

	return helper(start)
}

func canReach(arr []int, start int) bool {
	n := len(arr)
	visited := make([]bool, n)
	queue := []int{start}
	visited[start] = true

	for len(queue) > 0 {
		i := queue[0]
		queue = queue[1:]

		if arr[i] == 0 {
			return true
		}

		for _, next_i := range []int{i + arr[i], i - arr[i]} {
			if next_i >= 0 && next_i < n && !visited[next_i] {
				visited[next_i] = true
				queue = append(queue, next_i)
			}
		}
	}

	return false
}
