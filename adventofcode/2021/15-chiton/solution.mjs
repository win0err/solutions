const parseInput = input => input
  .trim()
  .split('\n')
  .map(
    line => line
      .split('')
      .map(ch => parseInt(ch, 10))
  )

class Queue {
  constructor() {
    this.data = new Map()
  }

  get size() {
    return this.data.size
  }

  enqueue(value, priority = 0) {
    this.data.set(value, priority)
  }

  dequeue() {
    const found = { priority: Infinity, value: undefined }

    this.data.forEach((priority, value) => {
      if (found.priority > priority) {
        found.value = value
        found.priority = priority
      }
    })

    this.data.delete(found.value)

    return found.value
  }
}

const getShortestPath = (graph, start, end) => {
  if (start === end) return 0

  const nodes = Object.keys(graph)

  const distances = new Map(nodes.map(node => [node, Infinity]))
  distances.set(start, 0)

  const previousNodes = new Map(nodes.map(node => [node, null]))

  const nodeQueue = new Queue() // MinHeap would be better, but I'm lazy
  nodeQueue.enqueue(start, 0)

  while (nodeQueue.size > 0) {
    const currentNode = nodeQueue.dequeue()
    const neighbors = graph[currentNode]

    Object.keys(neighbors).forEach(node => {
      const currentDistanceFromStart = neighbors[node] + distances.get(currentNode)

      if (currentDistanceFromStart < distances.get(node)) {
        nodeQueue.enqueue(node, currentDistanceFromStart)
        distances.set(node, currentDistanceFromStart)
        previousNodes.set(node, currentNode)
      }
    })
  }

  if (!previousNodes.get(end)) {
    throw new Error(`Path to the ${end} node is not exists!`)
  }

  return distances.get(end)
}

const getFullMap = (map) => {
  const extendedMap = []

  const cols = map[0].length
  const rows = map.length

  for (let mulRow = 0; mulRow < 5; mulRow++) {
    for (let mulCol = 0; mulCol < 5; mulCol++) {
      for (let r = 0; r < rows; r++) {
        for (let c = 0; c < cols; c++) {
          const x = r + rows * mulRow
          const y = c + cols * mulCol

          if (!extendedMap[x]) extendedMap[x] = []
          extendedMap[x][y] = ((map[r][c] + mulRow + mulCol - 1) % 9) + 1
        }
      }
    }
  }

  return extendedMap
}

const h = (x, y) => `${x}_${y}`

const getNeighboursFn = matrix => {
  const colsCount = matrix[0].length
  const rowsCount = matrix.length

  return (row, col) => [
    [row - 1, col],
    [row + 1, col],
    [row, col - 1],
    [row, col + 1],
  ].filter(([r, c]) => r >= 0 && r < rowsCount && c >= 0 && c < colsCount)
}

const createGraphFromMap = (map) => {
  const getNeighbours = getNeighboursFn(map)
  const graph = {}

  for (let i = 0; i < map.length; i++) {
    for (let j = 0; j < map[0].length; j++) {
      const key = h(i, j)
      graph[key] = getNeighbours(i, j).reduce(
        (acc, [col, row]) => {
          acc[h(col, row)] = map[col][row]

          return acc
        },
        {},
      )
    }
  }

  return graph
}

const getStartEnd = map => ({
  start: h(0, 0),
  end: h(map.length-1, map[0].length-1),
})


const task1 = map => {
  const graph = createGraphFromMap(map)
  const { start, end } = getStartEnd(map)

  return getShortestPath(graph, start, end)
}

const task2 = map => {
  const fullMap = getFullMap(map)

  const graph = createGraphFromMap(fullMap)
  const { start, end } = getStartEnd(fullMap)

  return getShortestPath(graph, start, end)
}


export default {
  parseInput,
  task1,
  task2,
}
