import { maxHeapify, parent } from './heap.mjs'


export const heapMaximum = A => A[0]

export const heapExtractMaximum = (A) => {
	if (!A.length) throw new Error('Queue is empty')

	const max = heapMaximum(A)
	A[0] = A.pop()

	maxHeapify(A, 0)

	return max
}

export const heapIncreaseKey = (A, i, key) => {
	if (key < A[i]) throw new Error('New key is smaller than current key')

	A[i] = key

	while (i > 0 && A[parent(i)] < A[i]) {
		[A[i], A[parent(i)]] = [A[parent(i)], A[i]]
		i = parent(i)
	}
}

export const maxHeapInsert = (A, key) => {
	A.push(key-1) // or -Infinity
	heapIncreaseKey(A, A.length-1, key)
}
