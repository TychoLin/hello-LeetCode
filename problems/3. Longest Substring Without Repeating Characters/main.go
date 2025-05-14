func lengthOfLongestSubstring(s string) int {
	charSet := make(map[byte]bool)
	left, maxLen := 0, 0

	for right := 0; right < len(s); right++ {
		for charSet[s[right]] {
			delete(charSet, s[left])
			left++
		}
		charSet[s[right]] = true
		maxLen = max(maxLen, right-left+1)
	}

	return maxLen
}
