function isIsomorphic(s: string, t: string): boolean {
	if (s.length !== t.length)
		return false

	const s2t = {}
	const t2s = {}

	for (let i = 0; i < s.length; i++) {
		let sc = s[i], tc = t[i]

		if (s2t[sc] && s2t[sc] !== tc || t2s[tc] && t2s[tc] !== sc)
			return false

		s2t[sc] = tc
		t2s[tc] = sc
	}

	return true
}
