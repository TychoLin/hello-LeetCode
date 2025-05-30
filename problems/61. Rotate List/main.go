func rotateRight(head *ListNode, k int) *ListNode {
	if head == nil || head.Next == nil || k == 0 {
		return head
	}

	tail := head
	counter := 1
	for tail.Next != nil {
		tail = tail.Next
		counter += 1
	}

	k %= counter
	if k == 0 {
		return head
	}

	tail.Next = head

	new_tail := head
	for i := 0; i < counter-k-1; i++ {
		new_tail = new_tail.Next
	}

	new_head := new_tail.Next
	new_tail.Next = nil

	return new_head
}
