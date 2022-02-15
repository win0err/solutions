const parseInput = input => input.split('\n').map(line => parseInt(line.split(':')[1], 10))

const cached = (fn) => {
  const cache = {}

  return (...args) => {
    const hash = JSON.stringify(args)

    if (!cache[hash]) {
      cache[hash] = fn(...args)
    }

    return cache[hash]
  }
}

const createPlayer = ({ position = 0, score = 0 } = {}) => ({
  score,
  position,
  move(steps) {
    this.position = (this.position + steps - 1) % 10 + 1
    this.score += this.position
  }
})

const MAX_SCORE_DETERMINISTIC = 1_000
const MAX_SCORE_DIRAC = 21

const playDeterministic = (player, opponent, dice = 1) => {
  if (opponent.score >= MAX_SCORE_DETERMINISTIC) {
    return { looser: player, dice: dice - 1 }
  }

  player.move(dice*3 + 3)

  return playDeterministic(opponent, player, dice+3)
}


const playDirac = cached((player, opponent) => {
  if (opponent.score >= MAX_SCORE_DIRAC) return [0, 1]

  const victories = [0, 0]

  for (let dice1 of [1, 2, 3]) {
    for (let dice2 of [1, 2, 3]) {
      for (let dice3 of [1, 2, 3]) {
        // the universe splits at the moment
        const playerCopy = createPlayer(player)
        playerCopy.move(dice1 + dice2 + dice3)

        const [win2, win1] = playDirac(opponent, playerCopy)
        victories[0] += win1
        victories[1] += win2
      }
    }
  }

  return victories
})


const task1 = ([pos1, pos2]) => {
  const player1 = createPlayer({ position: pos1 })
  const player2 = createPlayer({ position: pos2 })
  const { looser, dice } = playDeterministic(player1, player2)

  return looser.score * dice
}

const task2 = ([pos1, pos2]) => {
  const player1 = createPlayer({ position: pos1 })
  const player2 = createPlayer({ position: pos2 })

  return Math.max(...playDirac(player1, player2))
}


export default {
  parseInput,
  task1,
  task2,
}
