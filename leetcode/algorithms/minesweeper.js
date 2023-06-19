const updateBoard = (board, [cy, cx]) => {
	if (board[cy][cx] === 'M') {
		board[cy][cx] = 'X'

		return board
	}

	const M = board[0].length
	const N = board.length

	const getNeighbours = (r, c) => [
		[0, -1], [0, 1], [1, 0], [-1, 0],
		[-1, -1], [1, 1], [-1, 1], [1, -1],
	]
		.map(([dy, dx]) => [dy + r, dx + c])
		.filter(([y, x]) => y >= 0 && x >= 0 && y < N && x < M)

	const queue = [[cy, cx]]
	while (queue.length > 0) {
		const [r, c] = queue.shift()

		if (board[r][c] !== 'E') continue

		const neighbours = getNeighbours(r, c)
		const minesCount = neighbours
			.reduce((a, [y, x]) => a + Number(board[y][x] === 'M'), 0)

		board[r][c] = minesCount ? String(minesCount) : 'B'

		if (minesCount === 0) {
			queue.push(...neighbours)
		}
	}

	return board
}
