class ListNode {
	constructor(val, next) {
		this.val = (val === undefined ? 0 : val)
		this.next = (next === undefined ? null : next)
	}
}

const addTwoNumbers = (l1, l2) => {
	const head = new ListNode(0)
	let current = head

	let remaining = 0
	while (l1 || l2) {
		current.next = new ListNode(remaining)
		current = current.next

		if (l1) {
			current.val += l1.val
			l1 = l1.next
		}

		if (l2) {
			current.val += l2.val
			l2 = l2.next
		}

		remaining = current.val >= 10 ? 1 : 0
		current.val = current.val % 10
	}

	if (remaining === 1) {
		current.next = new ListNode(remaining)
	}

	return head.next
}
