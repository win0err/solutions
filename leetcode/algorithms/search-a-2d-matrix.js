const searchMatrixImproved = (matrix, target) => {
    const m = matrix.length, n = matrix[0].length

    if (target < matrix[0][0] || target > matrix[m-1][n-1]) {
        return false
    }

    let r, c
    let minIdx = 0, maxIdx = m*n, midIdx

    while (maxIdx >= minIdx) {
        midIdx = minIdx + Math.floor((maxIdx-minIdx)/2)
        r = Math.floor(midIdx / n)
        c = midIdx % n

        if (target === matrix[r][c]) {
            return true
        } else if (target < matrix[r][c]) {
            maxIdx = midIdx - 1
        } else if (target > matrix[r][c]) {
            minIdx = midIdx + 1
        }
    }

    return false
}


const searchMatrix = (matrix, target) => {
    const m = matrix.length - 1, n = matrix[0].length - 1

    if (target < matrix[0][0] || target > matrix[m][n]) {
        return false
    }

    let row
    let minIdx = 0, maxIdx = m, midIdx

    while (maxIdx >= minIdx) {
        midIdx = minIdx + Math.floor((maxIdx-minIdx)/2)

        if (target >= matrix[midIdx][0] && target <= matrix[midIdx][n]) {
            row = matrix[midIdx]
            break
        } else if (target < matrix[midIdx][0]) {
            maxIdx = midIdx - 1
        } else if (target > matrix[midIdx][n]) {
            minIdx = midIdx + 1
        }
    }

    minIdx = 0, maxIdx = n

    while (maxIdx >= minIdx) {
        midIdx = minIdx + Math.floor((maxIdx-minIdx)/2)

        if (target === row[midIdx]) {
            return true
        } else if (target < row[midIdx]) {
            maxIdx = midIdx - 1
        } else if (target > row[midIdx]) {
            minIdx = midIdx + 1
        }
    }

    return false
}
