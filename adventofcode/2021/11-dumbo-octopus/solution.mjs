const parseInput = input => input
  .trim()
  .split('\n')
  .map(line => line
    .split('')
    .map(ch => parseInt(ch, 10))
  )

const getNeighboursFn = matrix => {
  const colsCount = matrix[0].length
  const rowsCount = matrix.length
  
  return (row, col) => [
    [row - 1, col - 1],
    [row - 1, col],
    [row - 1, col + 1],
    [row + 1, col - 1],
    [row + 1, col],
    [row + 1, col + 1],
    [row, col - 1],
    [row, col + 1],
  ].filter(([r, c]) => r >= 0 && r < rowsCount && c >= 0 && c < colsCount)
}

const range = n => [...Array(n).keys()]

const executeStep = (matrix) => {
  const getNeighbours = getNeighboursFn(matrix)

  // 1.
  matrix = matrix.map(row => row.map(v => v + 1))

  // 2.
  // Already processed flashing octopuses will have Infinity value
  const isNewFlash = (r, c) => matrix[r][c] > 9 && matrix[r][c] < Infinity

  const processingQueue = range(matrix.length)
    .map(r => range(matrix[0].length).map(c => [r, c]))
    .flat()
    .filter(([r, c]) => isNewFlash(r, c))
  
  const isAlreadyProcessing = (row, col) => processingQueue
    .find(([r, c]) => r === row && c === col)

  let flashes = 0
  while (processingQueue.length > 0) {
    const [row, col] = processingQueue.pop()
    matrix[row][col] = Infinity
    flashes += 1

    for (const [r, c] of getNeighbours(row, col)) {
      matrix[r][c] += 1
      if (isNewFlash(r, c) && !isAlreadyProcessing(r, c)) {
        processingQueue.push([r, c])
      } 
    }
  }

  // 3.
  matrix = matrix.map(row => row.map(v => v > 9 ? 0 : v))

  return { matrix, flashes }
}


const task1 = matrix => {
  let flashes = 0
  
  for (let i = 0; i < 100; i++) {
    const data = executeStep(matrix)

    matrix = data.matrix
    flashes += data.flashes
  }

  return flashes
}

const task2 = matrix => {
  let step = 0
  
  for (step = 0; matrix.flat().some(n => n !== 0); step++) {
    matrix = executeStep(matrix).matrix
  }

  return step
}


export default {
  parseInput,
  task1,
  task2,
}