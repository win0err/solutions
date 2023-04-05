const partitionString = (s) => {
	let count = 0

	const mem = new Set()
	for (const ch of s) {
		if (mem.has(ch)) {
			count += 1
			mem.clear()
		}

		mem.add(ch)
	}

	return count + 1
}
