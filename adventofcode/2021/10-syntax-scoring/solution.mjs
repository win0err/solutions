const parseInput = input => input
  .trim()
  .split('\n')

const resultTypes = {
  CORRUPTED: 'corrupted',
  INCOMPLETE: 'incomplete',
  OK: 'ok',
}

const analyzeBrackets = brackets => {
  const complementBrackets = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
  }

  const stack = []

  for(const bracket of brackets) {
    if (complementBrackets[bracket]) {
      stack.push(complementBrackets[bracket])
    } else {
      if (stack.pop() !== bracket) {
        return {
          type: resultTypes.CORRUPTED,
          bracket,
        }
      }
    }
  }

  if (stack.length > 0) {
    return {
      type: resultTypes.INCOMPLETE,
      completion: stack.reverse(),
    }
  }

  return { type: resultTypes.OK }
}


const corruptedScores = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137,
}

const task1 = input => input
  .map(analyzeBrackets)
  .filter(({ type }) => type === resultTypes.CORRUPTED)
  .map(({ bracket }) => corruptedScores[bracket])
  .reduce((sum, v) => sum + v, 0)

const incompleteScores = {
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4,
}

const task2 = input => {
  const scores = input
    .map(analyzeBrackets)
    .filter(({ type }) => type === resultTypes.INCOMPLETE)
    .map(({ completion }) => completion.reduce(
      (score, ch) => score * 5 + incompleteScores[ch],
      0, 
    ))
    .sort((a, b) => b - a)
  
  return scores[Math.floor(scores.length / 2)]
}
  

export default {
  parseInput,
  task1,
  task2,
}