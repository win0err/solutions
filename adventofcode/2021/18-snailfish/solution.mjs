const parseInput = input => input.split('\n').map(line => JSON.parse(line))

class Node {
  constructor(parent = null) {
    this.parent = parent

    this.value = null

    this.left = null
    this.right = null
  }
}

const createTree = (value, parent = null) => {
  const node = new Node(parent)

  if (Array.isArray(value)) {
    node.left = createTree(value[0], node)
    node.right = createTree(value[1], node)
  } else {
    node.value = value
  }

  return node
}

const getRegularValue = (startNode, side) => {
  const oppositeSide = { right: 'left', left: 'right' }[side]

  let prevVisited = startNode
  let currentNode = startNode.parent

  while (currentNode) {
    if (currentNode[side] !== prevVisited) {
      currentNode = currentNode[side]

      while (currentNode.value === null) {
        currentNode = currentNode[oppositeSide]
      }

      return currentNode
    }

    prevVisited = currentNode
    currentNode = currentNode.parent
  }

  return null
}

const nextNodeByType = (node, action, lvl = 0) => {
  if (lvl === 5 && action === 'explode') return node.parent
  if (node.value >= 10 && action === 'split') return node

  let leftResult = null
  let rightResult = null

  if (node.left) leftResult = nextNodeByType(node.left, action, lvl+1)
  if (node.right) rightResult = nextNodeByType(node.right, action, lvl+1)

  return leftResult || rightResult
}

const nextNode = (node) => {
  let found

  if (found = nextNodeByType(node, 'explode')) {
    return { node: found, action: 'explode' }
  }

  if (found = nextNodeByType(node, 'split')) {
    return { node: found, action: 'split' }
  }

  return null
}



const split = (node) => {
  if (node.value === null || node.value < 10) return node

  node.left = new Node(node)
  node.left.value = Math.floor(node.value/2)

  node.right = new Node(node)
  node.right.value = Math.ceil(node.value/2)

  node.value = null

  return node
}

const explode = (node) => {
  let left, right

  if (left = getRegularValue(node, 'left')) {
    left.value = left.value + node.left.value
  }

  if (right = getRegularValue(node, 'right')) {
    right.value = right.value + node.right.value
  }

  node.left = null
  node.right = null
  node.value = 0

  return node
}


const solve = tree => {
  let next
  const actions = { explode, split }

  while (next = nextNode(tree)) {
    actions[next.action](next.node)
  }

  return tree
}

const concatTrees = (left, right) => {
  const node = new Node()

  node.left = left
  node.right = right

  left.parent = node
  right.parent = node

  return node
}

const calcMagnitude = (node) => {
  if (node.value !== null) return node.value

  return calcMagnitude(node.left) * 3 + calcMagnitude(node.right) * 2
}


const task1 = arrays => calcMagnitude(
  arrays.map(createTree).reduce((result, tree) => solve(concatTrees(result, tree)))
)

const task2 = arrays => {
  let maxMagnitude = 0

  for (let i = 0; i < arrays.length; i++) {
    for (let j = i; j < arrays.length; j++) {
      const a = createTree(arrays[i])
      const b = createTree(arrays[j])

      const tree = solve(concatTrees(a, b))
      const magnitude = calcMagnitude(tree)

      if (magnitude > maxMagnitude) {
        maxMagnitude = magnitude
      }
    }
  }

  return maxMagnitude
}


export default {
  parseInput,
  task1,
  task2,
}
