import { buildMaxHeap, maxHeapify } from './heap.mjs'


export const heapsort = (A) => {
	buildMaxHeap(A)

	let heapSize = A.length
	for (let i = A.length-1; i >= 1; i--) {
		[A[0], A[i]] = [A[i], A[0]]
		maxHeapify(A, 0, --heapSize)
	}
}
