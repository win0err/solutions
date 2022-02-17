const merge = intervals => {
  const [firstInterval, ...sortedIntervals] = intervals.sort((a, b) => a[0] - b[0])
  let processingInterval = firstInterval

  const mergedIntervals = []
  sortedIntervals.forEach(([start, end]) => {
    if (start > processingInterval[1]) {
      mergedIntervals.push(processingInterval)
      processingInterval = [start, end]
    } else {
      processingInterval[1] = Math.max(end, processingInterval[1])
    }
  })

  return [...mergedIntervals, processingInterval]
}
