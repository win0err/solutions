const parseInput = input => {
  let [template, rules] = input.split('\n\n')
  
  rules = rules
    .split('\n')
    .reduce(
      (acc, l) => {
        const key = l[0] + l[1]
        const value = l[0] + l[6] + l[1]

        acc[key] = value

        return acc
      },
      {},
    )

  return { template, rules }
}


const cached = (fn) => {
  const cache = {}

  return (...args) => {
    const hash = args.join('_')
    
    if (!cache[hash]) {
      cache[hash] = fn(...args)
    }

    return cache[hash]
  }
}

const createPairs = function* (iterable) {
  const iterator = iterable[Symbol.iterator]()
  let [current, next] = [iterator.next(), iterator.next()]

  while (!next.done) {
      yield current.value + next.value;

      [current, next] = [next, iterator.next()]
  }
}

const createCounter = () => new Proxy({}, {
  get: (target, name) => target.hasOwnProperty(name) ? target[name] : 0,
})

const mergeCounters = (counter1, counter2) => {
  let result = createCounter()

  const keys = [...Object.keys(counter1), ...Object.keys(counter2)]
  for (const key of keys) {
    result[key] = counter1[key] + counter2[key]
  }

  return result
}

const solve = (initialTemplate, rules, totalIterations) => {
  const count = cached((template, iterations) => {
    let counter = createCounter()
  
    if (iterations > 0) {
      for (const pair of createPairs(template)) {
        const middleChar = rules[pair][1]
        counter[middleChar] += 1
        
        counter = mergeCounters(
          counter,
          count(rules[pair], iterations - 1)
        )
      }
    }
  
    return counter
  })

  const counter = count(initialTemplate, totalIterations)

  for (const char of initialTemplate) {
    counter[char] += 1
  }

  const values = Object.values(counter)

  return Math.max(...values) - Math.min(...values)
}


const task1 = ({ template, rules }) => solve(template, rules, 10)

const task2 = ({ template, rules }) => solve(template, rules, 40)


export default {
  parseInput,
  task1,
  task2,
}