func reverseList(head *ListNode) *ListNode {
	var prev *ListNode = nil
	cur := head

	for cur != nil {
		newCur := cur.Next
		cur.Next = prev
		prev = cur
		cur = newCur
	}

	return prev
}
