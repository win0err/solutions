const parseInput = input => input
  .split('\n')
  .map(line => line.split('-'))

const clone = o => ({ ...o})

class Graph {
  static START = 'start'
  static END = 'end'

  constructor(edges = []) {
    this.vertices = {}
    this.allowTwice = false

    edges.forEach(edge => this.addEdge(...edge))
  }

  get startVertex() {
    return this.vertices[Graph.START]
  }

  addEdge(v1, v2) {
    for (const edge of [v1, v2]) {
      if (!this.vertices[edge]) {
        this.vertices[edge] = {
          name: edge,
          neighbours: [],
          isRevisitAllowed: edge.toLowerCase() !== edge,
          isStartVertex: edge === Graph.START,
          isEndVertex: edge === Graph.END,
        }
      }
    }

    this.vertices[v1].neighbours.push(v2)
    this.vertices[v2].neighbours.push(v1)
  }

  count(v = this.startVertex, visited = {}) {
    if (v.isEndVertex) {
      return 1
    }

    if (visited[v.name] && (!this.allowTwice || Object.values(visited).includes(2) || v.isStartVertex)) {
      return 0
    }
    
    if (!v.isRevisitAllowed) {
      visited[v.name] = !visited[v.name] ? 1 : 2
    }
    
    let pathsCount = 0
    for (let name of v.neighbours) {            
      pathsCount += this.count(this.vertices[name], clone(visited))
    }

    return pathsCount
  }
}


const task1 = edges => {
  const graph = new Graph(edges);
  graph.allowTwice = false

  return graph.count()
}

const task2 = edges => {
  const graph = new Graph(edges);
  graph.allowTwice = true

  return graph.count()
}


export default {
  parseInput,
  task1,
  task2,
}