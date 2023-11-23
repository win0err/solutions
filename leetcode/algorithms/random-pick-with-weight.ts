class Solution {
	sums: number[]

	constructor(weights: number[]) {
		this.sums = weights.reduce(
			(sums, weight, idx) => {
				const prevSum = sums[idx - 1] || 0
				sums.push(prevSum + weight)

				return sums
			},
			[] as number[],
		)
	}

	pickIndex(): number {
		const pickedValue = Math.trunc(Math.random() * this.sums[this.sums.length - 1])

		let l = 0, r = this.sums.length - 1, mid
		while (l <= r) {
			mid = Math.trunc((r - l) / 2) + l

			if (pickedValue >= this.sums[mid]) l = mid + 1
			else r = mid - 1
		}

		return l
	}
}
