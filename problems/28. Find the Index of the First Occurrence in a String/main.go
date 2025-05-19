func strStr(haystack string, needle string) int {
	n, m := len(haystack), len(needle)
	for i := 0; i <= n-m; i++ {
		k := 0
		for k < m && haystack[i+k] == needle[k] {
			k++
		}
		if k == m {
			return i
		}
	}
	return -1
}

func strStr(haystack string, needle string) int {
	n, m := len(haystack), len(needle)
	if m == 0 {
		return 0
	}

	last := make(map[rune]int)
	for k := 0; k < m; k++ {
		last[rune(needle[k])] = k
	}

	i := m - 1
	k := m - 1

	for i < n {
		if haystack[i] == needle[k] {
			if k == 0 {
				return i
			} else {
				i--
				k--
			}
		} else {
			j, exists := last[rune(haystack[i])]
			if !exists {
				j = -1
			}

			i += m - min(k, j+1)
			k = m - 1
		}
	}

	return -1
}
