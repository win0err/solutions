function reverseBetween(head: ListNode | null, left: number, right: number): ListNode | null {
	let i = 1
	let curr = head

	let leftHead = null
	let leftTail = null
	if (i < left) {
		leftHead = head

		for (i; i < left; i++) {
			leftTail = curr
			curr = curr.next
		}
	}

	let midHead = null
	let midTail = curr
	for (i; i <= right; i++) {
		const next = curr.next
		curr.next = midHead

		midHead = curr
		curr = next
	}

	// join left + middle + right lists
	const rightHead = curr
	midTail.next = rightHead

	if (leftHead) {
		leftTail.next = midHead
		return leftHead
	}

	return midHead
}
