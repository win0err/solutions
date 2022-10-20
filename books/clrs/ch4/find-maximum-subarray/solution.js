const findSum = (list) => {
    let sum = 0, bestSum = -Infinity
    list.forEach((el) => {
        sum = Math.max(el, sum+el)
        bestSum = Math.max(sum, bestSum)
    })

    return bestSum
}

const find = (list) => {
    let sum = 0, bestSum = -Infinity
    let bestLeft = 0, bestRight = 0, left = 0

    list.forEach((el, i) => {
        if (sum <= 0) {
            sum = 0
            left = i
        }

        sum += el

        if (sum > bestSum) {
            bestSum = sum
            bestRight = i
            bestLeft = left
        }
    })

    return {
        bestSum,
        subarray: list.slice(bestLeft, bestRight+1)
    }
}


const solutionA = find([13, -3, -25, 20, -3, -16, -23, 18, 20, -7, 12, -5, -22, 15, -4, 7]) // 18, 20, -7, 12 : 43
console.log(JSON.stringify(solutionA))

const solutionB = find([-23, -14, -24]) // -14 : -14
console.log(JSON.stringify(solutionB))
