const parseInput = input => {
  const [iea, rawImage] = input.trim().split('\n\n')
  const image = rawImage.split('\n').map(line => line.split(''))

  return { iea, image }
}


const codeToIndex = code => parseInt(
  code.replaceAll('.', 0).replaceAll('#', 1),
  2,
)

const infinityFiller = function* (iea) {
  let filledWith = '.' // initially filled with . (zeroes)

  do {
    yield filledWith

    // for random point in space: all neighbours are (filledWith's value)
    const willFilledNextWithIdx = codeToIndex(filledWith.repeat(9))
    filledWith = iea[willFilledNextWithIdx]
  } while (true)
}

const getCode = (image, [row, col], infinityFilledWith) => {
  const isNotInfinityImage = (r, c) => r >= 0 && r < image.length && c >= 0 && c < image[0].length

  return [
    [row - 1, col - 1],
    [row - 1, col],
    [row - 1, col + 1],
    [row, col - 1],
    [row, col],
    [row, col + 1],
    [row + 1, col - 1],
    [row + 1, col],
    [row + 1, col + 1],
  ].map(([r, c]) => isNotInfinityImage(r, c) ? image[r][c] : infinityFilledWith).join('')
}

const enhanceImage = ({ image, iea }, infinityFilledWith) => {
  const newImage = []

  // image will grow by 1 pixel from each side
  for (let r = -1; r < image.length + 1; r++) {
    for (let c = -1; c < image[0].length + 1; c++) {
      if (!newImage[r + 1]) newImage[r + 1] = []

      const code = getCode(image, [r, c], infinityFilledWith)
      const enhancedPixel = iea[codeToIndex(code)]

      newImage[r+1][c+1] = enhancedPixel
    }
  }

  return newImage
}

const solve = ({ image, iea }, iterations) => {
  const fillerGenerator = infinityFiller(iea)
  for (let i = 0, filler; i < iterations; i++) {
    filler = fillerGenerator.next()
    image = enhanceImage({ image, iea }, filler.value)
  }

  return image.flat().filter(ch => ch === '#').length
}

const task1 = parsedInput => solve(parsedInput, 2)
const task2 = parsedInput => solve(parsedInput, 50)


export default {
  parseInput,
  task1,
  task2,
}
