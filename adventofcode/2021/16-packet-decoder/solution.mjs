const parseInput = input => input
  .split('')
  .map(n => parseInt(n, 16).toString(2).padStart(4, '0'))
  .join('')

const createBitSlice = (bits) => {
  return {
    bits,
    get length() {
      return this.bits.length
    },
    read(length = this.bits.length) {
      const bits = this.bits.slice(0, length)
      this.bits = this.bits.slice(length)

      return bits
    },
    readAsNumber(length = this.bits.length) {
      return parseInt(this.read(length), 2)
    },
  }
}

// packet types
const ADD = 0
const PRODUCT = 1
const MIN = 2
const MAX = 3
const LITERAL = 4
const GREATER_THAN = 5
const LESS_THAN = 6
const EQUALS = 7

const decodePacket = (bits) => {
  const version = bits.readAsNumber(3)
  const typeID = bits.readAsNumber(3)

  let value, subPackets = []

  if (typeID === LITERAL) {
    let literal = '', isLast = false
    do {
      isLast = !bits.readAsNumber(1)
      literal += bits.read(4)
    } while(!isLast)

    value = createBitSlice(literal).readAsNumber()
  } else { // operator
    const lengthTypeID = bits.readAsNumber(1)

    if (lengthTypeID === 0) {
      const subPacketsLength = bits.readAsNumber(15)
      const subBits = createBitSlice(bits.read(subPacketsLength))

      while (subBits.length > 0) {
        subPackets.push(decodePacket(subBits))
      }
    } else {
      const subPacketsCount = bits.readAsNumber(11)

      for (let i = 0; i < subPacketsCount; i++) {
        subPackets.push(decodePacket(bits))
      }
    }
  }

  return { version, typeID, value, subPackets }
}

const countVersions = ({ version, subPackets }) => subPackets.reduce(
  (sum, packet) => sum + countVersions(packet),
  version,
)

const calculate = ({ subPackets = [], typeID, value }) => {
  const nestedValues = subPackets.map(calculate)
  switch (typeID) {
    case ADD: return nestedValues.reduce((a, b) => a + b, 0)
    case PRODUCT: return nestedValues.reduce((a, b) => a * b, 1)
    case MIN: return Math.min(...nestedValues)
    case MAX: return Math.max(...nestedValues)
    case LITERAL: return value
    case GREATER_THAN: return Number(nestedValues[0] > nestedValues[1])
    case LESS_THAN: return Number(nestedValues[0] < nestedValues[1])
    case EQUALS: return Number(nestedValues[0] === nestedValues[1])
  }
}


const task1 = parsedInput => countVersions(decodePacket(createBitSlice(parsedInput)))

const task2 = parsedInput => calculate(decodePacket(createBitSlice(parsedInput)))


export default {
  parseInput,
  task1,
  task2,
}
