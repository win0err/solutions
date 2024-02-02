function getIntersection([s1, e1], [s2, e2]) {
	if (e1 < s2 || e2 < s1)
		return null

	return [Math.max(s1, s2), Math.min(e1, e2)]
}

function intervalIntersection(
	list1: Array<[number, number]>,
	list2: Array<[number, number]>,
): Array<[number, number]> {
	const intersections = []

	let i1 = 0, i2 = 0
	while (i1 < list1.length && i2 < list2.length) {
		const found = getIntersection(list1[i1], list2[i2])

		if (found)
			intersections.push(found)

		const [, e1] = list1[i1]
		const [, e2] = list2[i2]

		if (e1 < e2)
			i1++
		else
			i2++
	}

	return intersections
}
