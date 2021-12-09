const parseInput = input => [...input.trim().matchAll(/(?<x1>\d+),(?<y1>\d+) -> (?<x2>\d+),(?<y2>\d+)/g)]
  .map(({ groups }) => Object.fromEntries(
    Object.entries(groups).map(
      ([k, v]) => [k, parseInt(v, 10)]
    )
  ))


const getDimension = lines => Math.max(...lines.map(coords => Object.values(coords)).flat()) + 1

const task1 = (lines) => {
  const dimension = getDimension(lines)
  const diagram = Array(dimension * dimension).fill(0)

  const linearLines = lines.filter(({ x1, x2, y1, y2 }) => x1 === x2 || y1 === y2)

  linearLines.forEach(({ x1, x2, y1, y2 }) => {
    for (let x = Math.min(x1, x2); x <= Math.max(x1, x2); x++) {
      for (let y = Math.min(y1, y2); y <= Math.max(y1, y2); y++) {
        diagram[x + y*dimension] += 1
      }
    }
  })

  return diagram.filter(n => n >= 2).length
}


const task2 = (lines) => {
  const dimension = getDimension(lines)
  const diagram = Array(dimension * dimension).fill(0)

  const linearLines = lines.filter(({ x1, x2, y1, y2 }) => x1 === x2 || y1 === y2)
  const diagonalLines = lines.filter(({ x1, x2, y1, y2 })  => x1 !== x2 && y1 !== y2)

  linearLines.forEach(({ x1, x2, y1, y2 }) => {
    for (let x = Math.min(x1, x2); x <= Math.max(x1, x2); x++) {
      for (let y = Math.min(y1, y2); y <= Math.max(y1, y2); y++) {
        diagram[x + y*dimension] += 1
      }
    }
  })

  diagonalLines.forEach(({ x1, x2, y1, y2 }) => {
    const xStep = x1 < x2 ? 1 : -1
    const yStep = y1 < y2 ? 1 : -1
    for (let x = x1, y = y1; x !== x2 + xStep; x += xStep, y += yStep) {
      diagram[x + y*dimension] += 1
    }
  })

  return diagram.filter(n => n >= 2).length
}


export default {
  parseInput,
  task1,
  task2,
}