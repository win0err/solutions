const numIslands = (grid) => {
	let numberOfIslands = 0

	const getNeighbourCoords = (x, y) => [[-1, 0], [1, 0], [0, -1], [0, 1]]
		  .map(([dx, dy]) => [x+dx, y+dy])

	const checkIsLand = (x, y) => grid[x]?.[y] === '1'
	const coordsToKey = (x, y) => `${x}:${y}`

	const visited = new Set()
	const visitIsland = (r, c) => {
		if (!checkIsLand(r, c) || visited.has(coordsToKey(r, c)))
			return

		numberOfIslands += 1

		const queue = [[r, c]]
		while (queue.length > 0) {
			const [x, y] = queue.pop() // DFS; use queue.shift() for BFS
			const key = coordsToKey(x, y)

			if (visited.has(key))
				continue

			visited.add(key)

			const landAroudCell = getNeighbourCoords(x, y)
				  .filter(coords => checkIsLand(...coords))

			queue.push(...landAroudCell)
		}
	}


	for (let r = 0; r < grid.length; r++) {
		for (let c = 0; c < grid[r].length; c++) {
			visitIsland(r, c)
		}
	}

	return numberOfIslands
}
