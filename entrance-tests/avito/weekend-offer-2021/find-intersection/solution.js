const SEPARATOR = ','

const parseCsv = str => str.trim().split(SEPARATOR).map(ch => ch.trim())


function findIntersection(strArray) { 
  const [first, second] = strArray.map(line => new Set(parseCsv(line)))

  const intersection = [...first].filter(el => second.has(el))

  return intersection.join(SEPARATOR)
}


export default {
  findIntersection,
}