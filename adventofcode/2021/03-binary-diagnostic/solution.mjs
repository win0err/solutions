const parseInput = input => input
  .trim()
  .split('\n')
  .map(line => line.split('').map(n => parseInt(n, 10)))


const transpose = matrix => matrix[0].map((_, colIdx) => matrix.map(row => row[colIdx]))
const bitsToNumber = bits => parseInt(bits.join(''), 2)

const task1 = (bitsMatrix) => {
  const tranposed = transpose(bitsMatrix)

  const gammaBits = tranposed.map(bitsAtPosition => {
    const onesCount = bitsAtPosition.filter(bit => bit === 1).length
    const zerosCount = bitsAtPosition.filter(bit => bit === 0).length
    
    return Number(onesCount > zerosCount)
  })

  const gamma = bitsToNumber(gammaBits)
  const bitMask = bitsToNumber(
    Array(bitsMatrix[0].length).fill(1)
  )

  return gamma * (gamma^bitMask)
}

const getStats = list => {
  const count = list.reduce(
    ([zeroes, ones], number) => [
      zeroes + Number(number === 0),
      ones + Number(number === 1),
    ],
    [0, 0]
  )

  return {
    mostCommon: Number(count[1] >= count[0]),
    lessCommon: Number(count[1] < count[0]),
  }
}

const task2 = bitsMatrix => {
  const reducedData = Array
    .from(Array(bitsMatrix[0].length).keys())
    .reduce(({ o2, co2 }, offset) => {
      if (o2.length > 1) {
        const o2Stats = getStats(o2.map(list => list[offset]))
        o2 = o2.filter(bit => bit[offset] === o2Stats.mostCommon)
      }

      if (co2.length > 1) {
        const co2Stats = getStats(co2.map(list => list[offset]))
        co2 = co2.filter(bit => bit[offset] === co2Stats.lessCommon)
      }
      
      return { o2, co2 }
    }, {
      o2: bitsMatrix,
      co2: bitsMatrix,
    })

  return bitsToNumber(reducedData.o2[0]) * bitsToNumber(reducedData.co2[0])
}


export default {
  parseInput,
  task1,
  task2,
}