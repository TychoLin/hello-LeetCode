func longestCommonPrefix(strs []string) string {
	// Use the first string as a reference
	prefix := strs[0]

	// Compare the prefix with each string in the array
	for i := 1; i < len(strs); i++ {
		// Reduce prefix until it's a prefix of the current string
		j := 0
		for j < len(prefix) && j < len(strs[i]) && prefix[j] == strs[i][j] {
			j++
		}

		// Update prefix to the common part
		prefix = prefix[0:j]

		// If prefix becomes empty, there's no common prefix
		if prefix == "" {
			return ""
		}
	}

	return prefix
}

func longestCommonPrefix(strs []string) string {
	n := len(strs[0])
	for i := 1; i < len(strs); i++ {
		if n > len(strs[i]) {
			n = len(strs[i])
		}
	}
	i := 0
	for i < n {
		c := strs[0][i]
		for j := 1; j < len(strs); j++ {
			if c != strs[j][i] {
				return strs[0][:i]
			}
		}
		i++
	}
	return strs[0][:i]
}
