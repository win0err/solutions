function findCircleNum(connections: number[][]): number {
	const isVisited = Array(connections.length).fill(false)

	const visitNeighbours = (city) => {
		if (isVisited[city]) return

		isVisited[city] = true

		for (const [other, isConnected] of Object.entries(connections[city])) {
			if (!isConnected) continue

			visitNeighbours(other)
		}
	}

	let provinces = 0
	for (const city in connections) {
		if (isVisited[city]) continue

		provinces++
		visitNeighbours(city)
	}

	return provinces
}
