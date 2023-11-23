function findDiagonalOrder(nums: number[][]): number[] {
	const result: number[] = []
	const queue: Array<[number, number]> = [[0, 0]]

	while (queue.length > 0) {
		const [y, x] = queue.shift()
		result.push(nums[y][x])

		if (x === 0 && y + 1 < nums.length)
			queue.push([y + 1, x])

		if (x + 1 < nums[y].length)
			queue.push([y, x + 1])
	}

	return result
}
