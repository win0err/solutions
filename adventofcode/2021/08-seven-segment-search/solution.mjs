const parseInput = input => input
  .trim()
  .split('\n')
  .map(row => row
    .split(' | ')
    .map(
      subStr => subStr
        .split(' ')
        .map(code => code
          .split('')
          .sort()
          .join(''),
        ),
    ),
  )

const getCode = (...segments) => [...new Set(segments)].sort().join('')
const and = (...bools) => bools.every(v => v === true)

const createPatternRecognizer = patterns => {
  const one = patterns.find(code => code.length === 2)
  const four = patterns.find(code => code.length === 4)
  const seven = patterns.find(code => code.length === 3)
  const eight = patterns.find(code => code.length === 7)

  const three = patterns.find(code => and(
    code.length === 5,
    [...one].every(ch => code.includes(ch)),
  ))

  const efSegments = [...four].filter(seg => !one.includes(seg))
  const five = patterns.find(code => and(
    code.length === 5,
    efSegments.every(ch => code.includes(ch))
  ))

  const two = patterns.find(code => code.length === 5 && ![three, five].includes(code))
  const nine = patterns.find(code => code.length === 6 && code === getCode(...one, ...five))


  const zero = patterns.find(code => and(
    code.length === 6,
    code !== nine,
    [...one].every(ch => code.includes(ch)),
  ))
  const six = patterns.find(code => code.length === 6 && ![zero, nine].includes(code))
  

  const mapping = {
    [zero]: 0,
    [one]: 1,
    [two]: 2,
    [three]: 3,
    [four]: 4,
    [five]: 5,
    [six]: 6,
    [seven]: 7,
    [eight]: 8,
    [nine]: 9,
  }

  return pattern => mapping[pattern]
}

const task1 = signals => signals.reduce(
  (count, [patterns, values]) => {
    const recognizer = createPatternRecognizer(patterns)

    return count + values.map(recognizer).filter(v => [1, 4, 7, 8].includes(v)).length
  },
  0,
)

const task2 = signals => signals.reduce(
  (count, [patterns, values]) => {
    const recognizer = createPatternRecognizer(patterns)

    return count + Number(values.map(recognizer).join(''))
  },
  0,
)
  

export default {
  parseInput,
  task1,
  task2,
}