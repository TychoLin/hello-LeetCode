func cleanSpaces(b []byte) []byte {
	n := len(b)
	k := 0
	i := 0

	for i < n {
		for i < n && b[i] == ' ' {
			i++
		}

		for i < n && b[i] != ' ' {
			b[k] = b[i]
			k++
			i++
		}

		for i < n && b[i] == ' ' {
			i++
		}
		if i < n {
			b[k] = ' '
			k++
		}
	}

	return b[:k]
}

func reverse(b []byte, left, right int) {
	for left < right {
		b[left], b[right] = b[right], b[left]
		left++
		right--
	}
}

func reverseWords(s string) string {
	b := []byte(s)
	b = cleanSpaces(b)
	reverse(b, 0, len(b)-1)

	start := 0
	for i := 0; i < len(b); i++ {
		if b[i] == ' ' {
			reverse(b, start, i-1)
			start = i + 1
		}
	}
	reverse(b, start, len(b)-1)

	return string(b)
}

func reverseWords(s string) string {
	words := strings.Fields(s)

	for i, j := 0, len(words)-1; i < j; i, j = i+1, j-1 {
		words[i], words[j] = words[j], words[i]
	}

	return strings.Join(words, " ")
}
