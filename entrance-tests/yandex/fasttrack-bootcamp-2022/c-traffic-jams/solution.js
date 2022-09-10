module.exports = function (data) {
    let timeToTarget
    let prevTimeToTarget = -Infinity

    return data.trucks
        .sort((a, b) => b.position - a.position)
        .reduce(
            (count, truck) => {
                timeToTarget = (data.target-truck.position) / truck.speed

                if (timeToTarget > prevTimeToTarget) {
                    prevTimeToTarget = timeToTarget
                    count++
                }

                return count
            },
            0,
        )
}
