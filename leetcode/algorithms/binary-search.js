const search = (nums, target) => {
    let minIdx = 0, maxIdx = nums.length - 1, idx

    while(minIdx <= maxIdx) {
        idx = minIdx + Math.ceil((maxIdx - minIdx) / 2)

        if (nums[idx] === target) {
            return idx
        } else if (nums[idx] < target) {
            minIdx = idx + 1
        } else if (nums[idx] > target) {
            maxIdx = idx - 1
        }
    }

    return -1
}
