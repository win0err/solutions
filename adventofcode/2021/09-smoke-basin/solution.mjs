const parseInput = input => input
  .trim()
  .split('\n')
  .map(line => line
    .split('')
    .map(n => parseInt(n, 10))
  )

const getNeighboursFn = matrix => {
  const colsCount = matrix[0].length
  const rowsCount = matrix.length

  return (row, col) => [
    [row - 1, col],
    [row + 1, col],
    [row, col - 1],
    [row, col + 1],
  ].filter(([r, c]) => r >= 0 && r < rowsCount && c >= 0 && c < colsCount)
}

const h = (row, col) => `${row}_${col}`

const getBazinSize = (
  matrix,
  visitedItems,
  [startRow, startCol],
) => {
  let size = 0
  const getNeighbours = getNeighboursFn(matrix)
  const visitingQueue = [[startRow, startCol]]

  while (visitingQueue.length > 0) {
    const [r, c] = visitingQueue.pop()
    const value = matrix[r][c]

    if (!visitedItems.has(h(r, c)) && value < 9) {      
      visitingQueue.push(...getNeighbours(r, c))
      
      visitedItems.add(h(r, c))
      size++
    }
  }

  return size
}

const task1 = matrix => {
  const getNeighbours = getNeighboursFn(matrix)

  return matrix.reduce((risk, row, rowIdx) => {
    row.forEach((value, colIdx) => {
      const neighbours = getNeighbours(rowIdx, colIdx)
      const isLowPoint = neighbours.every(([r, c]) => matrix[r][c] > value)

      if (isLowPoint) {
        risk += value + 1
      }
    })

    return risk
  }, 0)
}

const task2 = matrix => {
  const visitedItems = new Set()

  const bazins = matrix.reduce((acc, row, rowIdx) => {
    row.forEach((_, colIdx) => {
      if (!visitedItems.has(h(rowIdx, colIdx))) {
        acc.push(getBazinSize(matrix, visitedItems, [rowIdx, colIdx]))
      }
    })

    return acc
  })

  const [a, b, c] = bazins.sort((a, b) => b - a)

  return a * b * c
}
  

export default {
  parseInput,
  task1,
  task2,
}