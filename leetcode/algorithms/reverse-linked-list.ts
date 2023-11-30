function reverseList(head: ListNode | null): ListNode | null {
	let newHead = null

	let curr = head
	while (curr !== null) {
		let next = curr.next
		curr.next = newHead

		newHead = curr
		curr = next
	}

	return newHead
}
