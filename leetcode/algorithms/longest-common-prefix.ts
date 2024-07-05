function longestCommonPrefix(strs: string[]): string {
	if (strs.length < 2) return strs[0] ?? ''

	for (let i = 0; ; i++) {
		const ch = strs[0][i]

		for (let j = 1; j < strs.length; j++) {
			if (!ch || strs[j][i] !== ch) {
				return strs[j].slice(0, i)
			}
		}
	}
}
