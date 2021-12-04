const transpose = matrix => matrix[0].map((_, colIdx) => matrix.map(row => row[colIdx]))

const parseInput = input => {
  const lines = input.trim().split('\n')
  const numbers = lines[0].split(',').map(n => parseInt(n, 10))

  let boards = []
  for (let i = 2; i < lines.length; i+=6) {
    let board = { rows: [], cols: [] }
    for (let row = 0; row < 5; row++) {
      const line = lines[i + row].split(' ').filter(ch => ch !== '').map(n => parseInt(n, 10))
      board.rows.push(line)
    }
    board.cols = transpose(board.rows)
    boards.push(board)
  }
  
  return { numbers, boards }
}

const includesAll = (subarray, array) => subarray.every(v => array.includes(v))
const isBoardWon = (board, nums) => [...board.rows, ...board.cols]
  .map(line => includesAll(line, nums))
  .some(v => v === true)


const task1 = ({ numbers, boards }) => {
  let winner = null
  let openedNumbers = []
  for (let i = 1; i < numbers.length && !winner; i++) {
    openedNumbers = numbers.slice(0, i)

    for (const board of boards) {
      if (isBoardWon(board, openedNumbers)) {
        winner = board
        break
      }
    } 
  }

  const unmarkedNumsSum = winner.cols
    .flat()
    .filter(n => !openedNumbers.includes(n))
    .reduce((sum, a) => sum + a, 0)

  return unmarkedNumsSum * openedNumbers[openedNumbers.length - 1]
}

const task2 = ({ numbers, boards }) => {
  let winners = []
  let openedNumbers = []
  for (let i = 1; i < numbers.length && winners.length !== boards.length; i++) {
    openedNumbers = numbers.slice(0, i)

    for (const board of boards) {
      if (isBoardWon(board, openedNumbers) && !winners.includes(board)) {
        winners.push(board)
      }
    } 
  }

  const lastWinner = winners[winners.length - 1]
  const unmarkedNumsSum = lastWinner.cols
    .flat()
    .filter(n => !openedNumbers.includes(n))
    .reduce((sum, a) => sum + a, 0)

  return unmarkedNumsSum * openedNumbers[openedNumbers.length - 1]
}


export default {
  parseInput,
  task1,
  task2,
}