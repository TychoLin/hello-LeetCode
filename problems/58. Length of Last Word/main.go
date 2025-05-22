func lengthOfLastWord(s string) int {
	length := 0
	// Start from the end of the string
	i := len(s) - 1

	// Skip trailing spaces
	for i >= 0 && s[i] == ' ' {
		i--
	}

	// Count characters until we hit a space or the beginning of the string
	for i >= 0 && s[i] != ' ' {
		length++
		i--
	}

	return length
}
