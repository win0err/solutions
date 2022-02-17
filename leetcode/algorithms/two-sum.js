const twoSum = (nums, target) => {
  const indexes = new Map()

  for (const [idx, number] of nums.entries())  {
    const lookingFor = target - number

    if (indexes.has(lookingFor)) {
      return [indexes.get(lookingFor), idx]
    }

    indexes.set(number, idx)
  }
}
