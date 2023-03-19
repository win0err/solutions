export const parent = i => Math.floor((i-1)/2)

const left = i => 2*i + 1
const right = i => 2*i + 2

export const maxHeapify = (A, i, heapSize = A.length) => {
	const l = left(i), r = right(i)
	let largestIdx = i

	if (l <= heapSize-1 && A[l] > A[i]) {
		largestIdx = l
	}

	if (r <= heapSize-1 && A[r] > A[largestIdx]) {
		largestIdx = r
	}

	if (largestIdx !== i) {
		[A[i], A[largestIdx]] = [A[largestIdx], A[i]]

		maxHeapify(A, largestIdx, heapSize)
	}
}

export const buildMaxHeap = (A) => {
	for (let i = Math.floor((A.length-1)/2); i >= 0; i--) {
		maxHeapify(A, i)
	}
}
