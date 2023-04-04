const partitionLabels = (s) => {
	const lastOccurrences = {}

	for (const [idx, ch] of Object.entries(s)) {
		lastOccurrences[ch] = Number(idx)
	}

	const partitionSizes = []

	let l = 0
	while (l < s.length) {
		let r = lastOccurrences[s[l]]

		for (let i = l + 1; i < r; i++) {
			r = Math.max(r, lastOccurrences[s[i]])
		}

		partitionSizes.push(r - l + 1)

		l = r + 1
	}

	return partitionSizes
}
