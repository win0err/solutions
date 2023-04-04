const maxArea = (height) => {
	let l = 0, r = height.length - 1,
		max = -1

	while (l < r) {
		const w = r - l
		const h = Math.min(height[l], height[r])

		max = Math.max(max, w * h)

		if (height[l] > height[r])
			r -= 1
		else
			l += 1
	}

	return max
}
