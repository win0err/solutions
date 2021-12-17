const romanToNumberMapping = {
  I: 1,
  IV: 4,
  V: 5,
  IX: 9,
  X: 10,
  XL: 40,
  L: 50,
  XC: 90,
  C: 100,
  CD: 400,
  D: 500,
  CM: 900,
  M: 1000,
}

const romanToNumber = roman => roman
  .split('')
  .reduce(
    (result, ch, i) => {
      const nextCh = roman[i + 1] || 0
      const cur = romanToNumberMapping[ch]
      const next = romanToNumberMapping[nextCh]

      return result + (cur < next ? -cur : cur)
    },
    0,
  )

const numberToRoman = num => Object.entries(romanToNumberMapping)
  .sort(([, n1], [, n2]) => n2 - n1)
  .reduce(
    (result, [r, n]) => {
      const ch = Math.floor(num / n)
      num -= ch * n
      return result + r.repeat(ch)
    },
    '',
  )

const reduceRomanNumber = romanNum => numberToRoman(romanToNumber(romanNum))


export default {
  reduceRomanNumber,
}