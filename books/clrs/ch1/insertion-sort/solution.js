const insertionSortFromBook = (list) => {
    for (let i = 1; i < list.length; i++) {
        let current = list[i]

        let j
        for (j = i-1; j >= 0 && list[j] > current; j--) {
            list[j+1] = list[j];
        }

        list[j+1] = current
    }
}

const insertionSort = (list) => {
    for (let i = 1; i < list.length; i++) {
        for (let j = i; j > 0 && list[j-1] > list[j]; j--) {
            [list[j], list[j-1]] = [list[j-1], list[j]]
        }
    }
}

const unsorted= [-2, 99, 0, -743, 2, 3, 4]

const list1 = Array.from(unsorted)
insertionSortFromBook(list1)

console.log(JSON.stringify(list1))


const list2 = Array.from(unsorted)
insertionSort(list2)

console.log(JSON.stringify(list2))
