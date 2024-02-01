function mergeArrays(nums1: number[][], nums2: number[][]): number[][] {
	const result = []
	let n1 = 0, n2 = 0

	while (n1 < nums1.length && n2 < nums2.length) {
		if (nums1[n1][0] === nums2[n2][0]) {
			result.push([
				nums1[n1][0],
				nums1[n1][1] + nums2[n2][1]
			])
			n1++; n2++
		} else if (nums1[n1][0] < nums2[n2][0]) {
			result.push(nums1[n1])
		    n1++
        } else {
			result.push(nums2[n2])
			n2++
        }
    }

	while (n1 < nums1.length) {
		result.push(nums1[n1])
		n1++
	}

	while (n2 < nums2.length) {
		result.push(nums2[n2])
		n2++
    }

	return result
}
