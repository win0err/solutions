module.exports = function (data) {
    const isBits = v => v[0] === '0' || v[0] === '1'

    const solution = new Map()

    data.forEach(({ value, time }) => {
        if (!isBits(value)) return

        for (let i = 0; i < value.length; i++) {
            if (value[i] === '1') {
                solution.set(time + i, null)
            }
        }
    })

    data.forEach(({ value, time }) => {
        if (isBits(value)) return

        for (let i = 0; i < value.length; i++) {
            if (solution.has(time + i)) {
                solution.set(time + i, value[i])
            }
        }
    })

    return Array.from(solution.entries())
        .sort((a, b) => a[0] - b[0])
        .map(([_, char]) => char)
        .join('')
}
