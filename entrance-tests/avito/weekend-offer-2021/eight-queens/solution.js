const BOARD_SIZE = 8
const parseCoords = str => [str[1], str[3]].map(n => parseInt(n, 10) - 1)

const getOtherQueens = (queen, queens) => queens.filter(q => q !== queen)

const getPos = (x, y) => x + BOARD_SIZE*y
const isOnBoard = coords => coords.map(x => x >= 0 && x <= BOARD_SIZE).every(n => n === true)

const hasHorVerIntersection = (queen, otherQueens) => otherQueens
  .some(([x, y]) => queen[0] === x || queen[1] === y)

const hasDiagonalIntersection = (queen, otherQueens) => {
  let board = new Array(BOARD_SIZE*BOARD_SIZE).fill(false)

  board[getPos(...queen)] = true
  
  for (let x = queen[0], y = queen[1]; isOnBoard([x, y]); x += 1, y += 1) {
    board[getPos(x, y)] = true
  }

  for (let x = queen[0], y = queen[1]; isOnBoard([x, y]); x -= 1, y += 1) {
    board[getPos(x, y)] = true
  }

  for (let x = queen[0], y = queen[1]; isOnBoard([x, y]); x += 1, y -= 1) {
    board[getPos(x, y)] = true
  }

  for (let x = queen[0], y = queen[1]; isOnBoard([x, y]); x -= 1, y -= 1) {
    board[getPos(x, y)] = true
  }

  return otherQueens.some(q => board[getPos(...q)] === true)
} 

const eightQueens = (strArr) => {
  const queens = strArr.map(parseCoords)

  for (let queen of queens) {
    const otherQueens = getOtherQueens(queen, queens)

    if (
      hasHorVerIntersection(queen, otherQueens) || hasDiagonalIntersection(queen, otherQueens)
    ) return `(${queen[0]+1},${queen[1]+1})`
  }

  return 'true' 
}


export default {
  eightQueens,
}