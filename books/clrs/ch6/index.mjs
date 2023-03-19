import { buildMaxHeap } from './heap.mjs'
import { heapsort } from './heapsort.mjs'
import {
	heapMaximum,
	heapExtractMaximum,
	heapIncreaseKey,
	maxHeapInsert,
} from './priorityQueue.mjs'


const unsorted = [4, 1, 3, 2, 16, 9, 10, 14, 8, 7]

const maxHeap = Array.from(unsorted)
buildMaxHeap(maxHeap)

const sorted = Array.from(unsorted)
heapsort(sorted)

console.table({ unsorted, maxHeap, sorted })

console.group('Priority Queues')

const pq1 = Array.from(maxHeap)
console.log('Max:', heapMaximum(pq1))
console.table({ queue: pq1 })
console.log()

const pq2 = Array.from(maxHeap)
console.log('Max (extracted):', heapExtractMaximum(pq2))
console.table({ queue: pq2 })
console.log()

const pq3 = Array.from(maxHeap)
heapIncreaseKey(pq3, pq3.indexOf(4), 15)
console.log('Increased key from 4 to 15')
console.table({ before: maxHeap, after: pq3 })

const pq4 = Array.from(maxHeap);
const insertingElements = [5, 21]
insertingElements.forEach(el => maxHeapInsert(pq4, el))
console.log('Inserted elements:', ...insertingElements)
console.table({ queue: pq4 })

console.groupEnd()
