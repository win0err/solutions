const parseInput = input => input.trim().split(',').map(n => parseInt(n, 10))

const range = (size, startAt = 0) => [...Array(size).keys()].map(i => i + startAt)

const minMaxRange = array => range(
  Math.max(...array) - Math.min(...array),
  Math.min(...array),
)

const getBestPosition = (positions, calcFuelFn) => minMaxRange(positions)
  .reduce(
    (destination, to) => {
      const result = positions.reduce((sum, from) => sum + calcFuelFn(from, to), 0)

      return (result < destination) ? result : destination
    },
    +Infinity,
  )

const task1 = (positions) => getBestPosition(
  positions, 
  (a, b) => Math.abs(a - b),
)

const task2 = (positions) => getBestPosition(
  positions,
  (a, b) => {
    const n = Math.abs(a - b)

    return n * (n+1) / 2 // https://en.wikipedia.org/wiki/Triangular_number
  },
)


export default {
  parseInput,
  task1,
  task2,
}