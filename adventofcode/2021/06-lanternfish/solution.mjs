const parseInput = input => input.trim().split(',').map(n => parseInt(n, 10))


const solveTask = (fish, totalDays) => {
  let initialDays = fish.reduce(
    (days, fishInternalTimer) => { days[fishInternalTimer] += 1; return days },
    Array(9).fill(0) // 0..8 -- probable timer values
  )

  return Array(totalDays)
    .fill()
    .reduce(
      days => {
        let [fishCount, ...restCounts] = days
        restCounts[6] += fishCount

        return [...restCounts, fishCount]
      },
      initialDays,
    )
    .reduce((sum, n) => sum + n, 0)
}

const task1 = input => solveTask(input, 80)
const task2 = input => solveTask(input, 256)


export default {
  parseInput,
  task1,
  task2,
}