const isSymmetric = ({ left, right }) => {
	const queue = [[left, right]]

	while (queue.length > 0) {
		const [l, r] = queue.shift()

		if (!l && !r) continue
		if (l?.val !== r?.val)
			return false

		queue.push([l.left, r.right], [l.right, r.left])
	}

	return true
}
