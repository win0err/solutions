const isSameTree = (p, q) => {
	const queue = [[p, q]]

	while (queue.length > 0) {
		const [l, r] = queue.shift()

		if (l && r && l.val === r.val) {
			queue.push([l.left, r.left], [l.right, r.right])
		} else if (l || r) {
			return false
		}
	}

	return true
}
