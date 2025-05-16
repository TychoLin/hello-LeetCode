func isValid(s string) bool {
	lefty := "([{"
	righty := ")]}"
	stack := []byte{}

	for i := 0; i < len(s); i++ {
		c := s[i]
		if strings.Contains(lefty, string(c)) {
			stack = append(stack, c)
		} else if strings.Contains(righty, string(c)) {
			if len(stack) == 0 {
				return false
			}
			top := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			if strings.IndexByte(righty, c) != strings.IndexByte(lefty, top) {
				return false
			}
		}
	}

	return len(stack) == 0
}
