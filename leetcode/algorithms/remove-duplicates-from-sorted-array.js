const removeDuplicates = (nums) => {
  let lastUniqIdx = 0

  for (let idx = 1; idx < nums.length; idx++) {
    if (nums[lastUniqIdx] !== nums[idx]) {
      lastUniqIdx += 1
      nums[lastUniqIdx] = nums[idx]
    }
  }

  return lastUniqIdx + 1
}
