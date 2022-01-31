const parseInput = input => {
  const { xFrom, xTo, yFrom, yTo } = input.match(
    /target area: x=(?<xFrom>-?\d+)\.\.(?<xTo>-?\d+), y=(?<yFrom>-?\d+)\.\.(?<yTo>-?\d+)/
  ).groups

  return {
    x: {
      from: parseInt(xFrom, 10),
      to: parseInt(xTo, 10),
    },

    y: {
      from: parseInt(yFrom, 10),
      to: parseInt(yTo, 10),
    },

    isReached(x, y){
      return this.canReach(x, y) && x >= this.x.from && y <= this.y.to
    },

    canReach(x, y) {
      return x <= this.x.to && y >= this.y.from
    },
  }
}

const calc = (targetArea, xV, yV) => {
  let x = 0, y = 0
  let maxHeight = y
  let isReached = false

  while (targetArea.canReach(x, y) && !isReached) {
    x += xV
    y += yV

    if (xV > 0) xV--
    if (xV < 0) xV++
    yV--

    if (y > maxHeight) maxHeight = y
    isReached = targetArea.isReached(x, y)
  }

  return { isReached, maxHeight }
}

const LIMIT = 1_000

const getSolution = targetArea => {
  let count = 0
  let highest = -Infinity

  for (let xV = 0; xV < LIMIT; xV++) {
    for (let yV = -LIMIT; yV < LIMIT; yV++) {
      const { isReached, maxHeight } = calc(targetArea, xV, yV)

      if (isReached) {
        count++

        if (maxHeight > highest) {
          highest = maxHeight
        }
      }
    }
  }

  return { highest, count }
}

const task1 = targetArea => getSolution(targetArea).highest

const task2 = targetArea => getSolution(targetArea).count


export default {
  parseInput,
  task1,
  task2,
}
