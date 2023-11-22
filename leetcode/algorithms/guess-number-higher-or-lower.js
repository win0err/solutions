// predefined:
// const guess = num => Math.min(Math.max(pick - num, -1), 1)

const guessNumber = (n) => {
    let min = 1, max = n, mid

    while(true) {
        mid = min + Math.ceil((max - min) / 2)

        switch (guess(mid)) {
            case -1:  // mid > pick
                max = mid - 1
                break
            case 1:  // mid < pick
                min = mid + 1
                break
            case 0:
                return mid
        }
    }
}
