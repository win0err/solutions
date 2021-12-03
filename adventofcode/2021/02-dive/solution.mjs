const parseInput = input => input
  .trim()
  .split('\n')
  .map(line => line.split(' '))
  .map(([action, number]) => [action, parseInt(number, 10)]);


export const task1 = data => {
  const state = { x: 0, y: 0 }

  const actions = {
    up: n => state.y -= n,
    down: n => state.y += n,
    forward: n => state.x += n
  }

  data.map(([action, number]) => actions[action](number))

  return state.x * state.y
}

export const task2 = data => {
  const state = { x: 0, y: 0, aim: 0 }

  const actions = {
    up: n => state.aim -= n,
    down: n => state.aim += n,
    forward: n => {
      state.x += n
      state.y += n * state.aim
    }
  }

  data.map(([action, number]) => actions[action](number))

  return state.x * state.y
}


export default {
  parseInput,
  task1,
  task2,
}