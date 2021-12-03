const parseInput = input => input
  .trim()
  .split('\n')
  .map(n => parseInt(n, 10))


export const task1 = numbers => numbers.reduce(
  (count, v, idx, list) => list[idx-1] && v > list[idx-1] ? count + 1 : count,
  0,
)

export const task2 = numbers => {
  const windowSize = 3
  const getWindowSum = offset => numbers.slice(offset - windowSize + 1, offset + 1).reduce((sum, n) => sum + n, 0)

  let count = 0
  for (
    let i = windowSize, current = getWindowSum(i), previous = getWindowSum(i-1);
    i < numbers.length;
    i++, previous = current, current = getWindowSum(i)
  ) {
    if (current > previous) count++
  }

  return count
}


export default {
  parseInput,
  task1,
  task2,
}