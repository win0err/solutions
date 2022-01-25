const parseInput = input => {
  let [coordinates, foldLines] = input
    .split('\n\n')
    .map(section => section.split('\n'))
  
  coordinates = coordinates.map(l => l.split(',').map(ch => parseInt(ch, 10)))
  foldLines = foldLines
    .reduce(
      (acc, line) => {
        let { coordinate, value } = line.match(
          /fold along (?<coordinate>[xy])=(?<value>\d*)/
        ).groups

        value = parseInt(value, 10)

        acc.push({ coordinate, value })

        return acc
      },
      [],
    )
    .sort((a, b) => b - a) 

  return { coordinates, foldLines }
}


const getFoldedCoordinate = (coordinate, foldLine) => coordinate > foldLine 
  ? foldLine*2 - coordinate
  : coordinate

const max = (iterable, selectorFn) => Math.max(...Array.from(iterable.values()).map(selectorFn))

const h = (x, y) => `${x}_${y}`

const groupFoldLines = foldLines => foldLines.reduce(
  (acc, { coordinate, value }) => {
    acc[coordinate].push(value)

    return acc
  },
  { x: [], y: [] },
)

const getPrintableCoordinates = (coordinates, foldLines) => coordinates.reduce(
  (acc, [x, y]) => {
    x = foldLines.x.reduce(getFoldedCoordinate, x)
    y = foldLines.y.reduce(getFoldedCoordinate, y)

    acc.set(h(x, y), [x, y])

    return acc
  },
  new Map(),
)

const getCharacter = isPrintable => isPrintable ? '░░' : '  '


const task1 = ({ coordinates, foldLines }) => {
  const groupedFoldLines = groupFoldLines([ foldLines[0] ])
  const printableCoordinates = getPrintableCoordinates(coordinates, groupedFoldLines)

  return printableCoordinates.size
}

const task2 = ({ coordinates, foldLines }) => {
  const groupedFoldLines = groupFoldLines(foldLines)
  const printableCoordinates = getPrintableCoordinates(coordinates, groupedFoldLines)
  
  const maxValues = { 
    x: max(printableCoordinates, ([x, _]) => x),
    y: max(printableCoordinates, ([_, y]) => y)
  }
  
  let codeString = '\n'
  for (let y = 0; y <= maxValues.y; y++) {
    for (let x = 0; x <= maxValues.x; x++) {
      codeString += getCharacter(printableCoordinates.has(h(x, y)))
    }
    codeString += '\n'
  }
  
  return codeString
}


export default {
  parseInput,
  task1,
  task2,
}