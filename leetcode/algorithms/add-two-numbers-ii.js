class ListNode {
	constructor(val, next) {
		this.val = (val === undefined ? 0 : val)
		this.next = (next === undefined ? null : next)
	}
}

const addTwoNumbers = (l1, l2) => {
	const v1 = []
	const v2 = []

	while (l1) {
		v1.push(l1.val)
		l1 = l1.next
	}

	while (l2) {
		v2.push(l2.val)
		l2 = l2.next
	}

	let current = new ListNode()
	let remaining = 0

	while (v1.length || v2.length) {
		current.val = remaining
		current.val += v1.pop() || 0
		current.val += v2.pop() || 0

		remaining = current.val >= 10 ? 1 : 0
		current.val = current.val % 10

		const prev = current
		current = new ListNode()
		current.next = prev
	}

	if (remaining === 1) {
		current.val = 1

		return current
	}

	return current.next
}
