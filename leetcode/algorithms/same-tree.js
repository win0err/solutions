const isSameTree = (p, q) => {
	const queue = [[p, q]]

	while (queue.length > 0) {
		const [l, r] = queue.shift()

		if (!l && !r) continue
		if (l?.val !== r?.val)
			return false

		queue.push([l.left, r.left], [l.right, r.right])
	}

	return true
}
