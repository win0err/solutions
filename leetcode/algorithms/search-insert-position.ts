function searchInsert(nums: number[], target: number): number {
    let l = 0, r = nums.length-1

    let mid
    while (l <= r) {
        mid = Math.trunc((r - l) / 2) + l

        if (nums[mid] < target) l = mid + 1
        else if (nums[mid] > target) r = mid - 1
        else return mid
    }

    return l
};
